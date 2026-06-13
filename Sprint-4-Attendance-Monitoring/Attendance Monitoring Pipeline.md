## Technologies Used

### Face Detection

Model:

* det_10g.onnx

Purpose:

* Detect faces from live camera feed.

### Face Landmark Detection

Models:

* 1k3d68.onnx
* 2d106det.onnx

Purpose:

* Align detected faces before recognition.

### Face Recognition

Model:

* w600k_r50.onnx

Framework:

* InsightFace Buffalo-L

Purpose:

* Generate 512-dimensional facial embeddings.

### Runtime Engine

Framework:

* ONNX Runtime GPU

Provider:

* CUDAExecutionProvider

Purpose:

* Accelerate model inference using NVIDIA GPU.

### Attendance Database

Database:

* SQLite

File:

* erp.db

Purpose:

* Store attendance records.

### Evidence Storage

Directory:

* attendance_photos/

Purpose:

* Save attendance proof images.
