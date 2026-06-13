from flask import Flask, render_template, send_from_directory
import sqlite3
import os

app = Flask(__name__)

@app.route('/attendance_photos/<path:filename>')
def attendance_photo(filename):
    return send_from_directory(
        os.path.join(os.getcwd(), 'attendance_photos'),
        filename
    )

@app.route("/")
def dashboard():

    conn = sqlite3.connect("erp.db")
    cursor = conn.cursor()

    employees = cursor.execute(
        "SELECT employee_id,name,department,embedding_name FROM employees"
    ).fetchall()

    attendance_rows = cursor.execute(
        """
        SELECT employee_id,date,time,status,photo_path
        FROM attendance
        """
    ).fetchall()

    conn.close()

    attendance_map = {}

    for row in attendance_rows:
        attendance_map[row[0]] = {
            "date": row[1],
            "time": row[2],
            "status": row[3],
            "photo": row[4]
        }

    return render_template(
        "index.html",
        employees=employees,
        attendance_map=attendance_map
    )

if __name__ == "__main__":
    app.run(debug=True)