import sqlite3

employee_id = input("Employee ID: ")
name = input("Name: ")
department = input("Department: ")
embedding_name = input("Embedding Name: ")

conn = sqlite3.connect("erp.db")
cursor = conn.cursor()

cursor.execute("""
INSERT INTO employees
(employee_id, name, department, embedding_name, photo_path)
VALUES (?, ?, ?, ?, ?)
""", (
    employee_id,
    name,
    department,
    embedding_name,
    ""
))

conn.commit()
conn.close()

print("Employee Added Successfully")