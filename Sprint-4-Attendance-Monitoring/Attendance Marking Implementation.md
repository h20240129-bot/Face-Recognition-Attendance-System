## Actual Attendance Marking Workflow

### Step 1: Camera Feed Capture

OpenCV continuously captures frames from the webcam.

![Camera Feed](images/camera-feed.png)

### Step 2: Face Detection

The det_10g.onnx model detects faces in the incoming frame.

![Face Detection](images/face-detection.png)

### Step 3: Face Alignment

The landmark models:

* 1k3d68.onnx
* 2d106det.onnx

align facial features before recognition.

![Face Alignment](images/face-alignment.png)

### Step 4: Embedding Generation

The w600k_r50.onnx recognition model generates a 512-dimensional embedding vector.

![Embedding Generation](images/embedding-generation.png)

### Step 5: Embedding Matching

Generated embedding is compared with embeddings stored in the student database.

Matching method:

* Cosine Similarity
* Similarity Threshold

![Embedding Matching](images/embedding-matching.png)

### Step 6: Student Identification

If similarity exceeds threshold:

Student ID is identified.

Example:

Student ID: 0001

![Student Identification](images/student-identification.png)

### Step 7: Duplicate Attendance Check

System checks SQLite database:

erp.db

to verify whether attendance has already been marked for that student today.

![Duplicate Check](images/duplicate-check.png)

### Step 8: Attendance Recording

If attendance does not exist:

INSERT attendance record into database.

![Attendance Insert](images/attendance-insert.png)

### Step 9: Attendance Evidence Storage

The recognized image is stored inside:

attendance_photos/

Example:

attendance_photos/0001_20260613_083249.jpg

![Photo Saved](images/photo-saved.png)

### Step 10: Success Message

System displays:

Attendance Marked -> 0001

![Attendance Success](images/attendance-success.png)
