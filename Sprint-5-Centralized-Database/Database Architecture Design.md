# Database Architecture Design

## Objective

Design a centralized database architecture for storing attendance records.

## Step 1: Analyze Existing System

Current system stores:

* Student Information
* Face Embeddings
* Attendance Records
* Attendance Photos

![Current Architecture](images/current-architecture.png)

## Step 2: Identify Database Requirements

The centralized database must support:

* Student Registration
* Face Embedding Storage
* Attendance Records
* Attendance Reports
* Multi-user Access

![Requirements Analysis](images/database-requirements.png)

## Step 3: Design Database Tables

### Student Table

Fields:

* Student_ID
* Name
* Department
* Email

![Student Table](images/student-table.png)

### Face Embeddings Table

Fields:

* Student_ID
* Embedding_Data

![Embedding Table](images/embedding-table.png)

### Attendance Table

Fields:

* Student_ID
* Date
* Time
* Status
* Photo_Path

![Attendance Table](images/attendance-table.png)

## Step 4: Define Data Flow

Camera → Recognition → Database Verification → Attendance Update → Reporting

![Database Flow](images/database-flow.png)

## Conclusion

A centralized database architecture was designed to support attendance monitoring and reporting.
