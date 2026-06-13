# Database Integration Implementation

## Objective

Connect the attendance monitoring system with a centralized database.

## Technology Used

### Database

SQLite (Current Prototype)

File:

erp.db

### Future Migration

* MySQL
* PostgreSQL

## Step 1: Create Database

Created:

erp.db

using SQLite.

![Database Creation](images/database-creation.png)

## Step 2: Establish Database Connection

Implemented database connection module.

File:

database_connection.py

![Database Connection](images/database-connection.png)

## Step 3: Create Tables

Created:

* Students
* Face_Embeddings
* Attendance

tables.

![Table Creation](images/table-creation.png)

## Step 4: Integrate Recognition Module

Face recognition results are sent to the database layer.

![Recognition Integration](images/recognition-integration.png)

## Step 5: Verify Student Identity

Student ID retrieved from face recognition is verified against database records.

![Identity Verification](images/identity-verification.png)

## Step 6: Store Attendance Record

Attendance record inserted automatically.

![Attendance Storage](images/attendance-storage.png)

## Step 7: Save Attendance Evidence

Photo path stored in database.

Example:

attendance_photos/0001_20260613.jpg

![Photo Storage](images/photo-storage.png)

## Result

Attendance monitoring system successfully integrated with the centralized database.
