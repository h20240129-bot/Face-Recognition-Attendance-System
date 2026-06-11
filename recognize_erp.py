import cv2
import pickle
import insightface
import numpy as np
import time
import sqlite3
from datetime import datetime
from numpy.linalg import norm

app = insightface.app.FaceAnalysis(
    providers=['CUDAExecutionProvider']
)

app.prepare(
    ctx_id=0,
    det_size=(1024, 1024)
)

print("GPU Face Recognition ERP Started...")

with open("embeddings/face_embeddings.pkl", "rb") as f:
    known_embeddings = pickle.load(f)

def mark_attendance(embedding_name, frame):

    conn = sqlite3.connect("erp.db")
    cursor = conn.cursor()

    cursor.execute(
        "SELECT employee_id FROM employees WHERE embedding_name=?",
        (embedding_name,)
    )

    employee = cursor.fetchone()

    if employee is None:
        conn.close()
        return

    employee_id = employee[0]

    today = datetime.now().strftime("%Y-%m-%d")
    current_time = datetime.now().strftime("%H:%M:%S")

    cursor.execute(
        "SELECT * FROM attendance WHERE employee_id=? AND date=?",
        (employee_id, today)
    )

    if cursor.fetchone() is None:

        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")

        photo_file = (
            f"attendance_photos/"
            f"{employee_id}_{timestamp}.jpg"
        )

        cv2.imwrite(photo_file, frame)

        cursor.execute(
            """
            INSERT INTO attendance
            (employee_id,date,time,status,photo_path)
            VALUES (?,?,?,?,?)
            """,
            (
                employee_id,
                today,
                current_time,
                "Present",
                photo_file
            )
        )

        conn.commit()

        print(f"Attendance Marked -> {employee_id}")
        print(f"Photo Saved -> {photo_file}")

    conn.close()

cap = cv2.VideoCapture(0)

while True:

    ret, frame = cap.read()

    if not ret:
        break

    start = time.time()

    faces = app.get(frame)

    for face in faces:

        x1, y1, x2, y2 = face.bbox.astype(int)

        embedding = face.embedding

        best_match = "Unknown"
        best_score = 0

        for name, db_embedding in known_embeddings.items():

            similarity = np.dot(
                embedding,
                db_embedding
            ) / (
                norm(embedding) *
                norm(db_embedding)
            )

            if similarity > best_score:
                best_score = similarity
                best_match = name

        if best_score < 0.55:
            best_match = "Unknown"

        if best_match != "Unknown" and best_score >= 0.70:
            mark_attendance(best_match, frame)

        if best_score >= 0.85:
            color = (0, 255, 0)
        elif best_score >= 0.65:
            color = (0, 255, 255)
        else:
            color = (0, 0, 255)

        cv2.rectangle(
            frame,
            (x1, y1),
            (x2, y2),
            color,
            2
        )

        text = f"{best_match} : {best_score:.2f}"

        cv2.putText(
            frame,
            text,
            (x1, y1 - 10),
            cv2.FONT_HERSHEY_SIMPLEX,
            0.8,
            color,
            2
        )

    fps = 1 / (time.time() - start)

    cv2.putText(
        frame,
        f"FPS: {fps:.2f}",
        (20, 40),
        cv2.FONT_HERSHEY_SIMPLEX,
        1,
        (0, 255, 255),
        2
    )

    cv2.imshow("GPU Face Recognition ERP", frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()