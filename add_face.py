import cv2
import pickle
import insightface

name = input("Enter Employee Name: ")

app = insightface.app.FaceAnalysis(
    providers=['CUDAExecutionProvider']
)
app.prepare(ctx_id=0)

with open("embeddings/face_embeddings.pkl", "rb") as f:
    embeddings = pickle.load(f)

cap = cv2.VideoCapture(0)

print("Press S to save face")

while True:

    ret, frame = cap.read()

    faces = app.get(frame)

    for face in faces:

        x1, y1, x2, y2 = face.bbox.astype(int)

        cv2.rectangle(frame,(x1,y1),(x2,y2),(0,255,0),2)

        cv2.putText(
            frame,
            name,
            (x1,y1-10),
            cv2.FONT_HERSHEY_SIMPLEX,
            0.8,
            (0,255,0),
            2
        )

    cv2.imshow("Add Face", frame)

    key = cv2.waitKey(1)

    if key == ord('s') and len(faces) > 0:

        embeddings[name] = faces[0].embedding

        with open("embeddings/face_embeddings.pkl", "wb") as f:
            pickle.dump(embeddings, f)

        print(f"{name} added successfully")
        break

    elif key == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()