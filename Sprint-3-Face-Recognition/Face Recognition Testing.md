## Testing Workflow

### Step 1: Start Camera

Started live camera feed.

![Camera Start](images/camera-start.png)

### Step 2: Detect Face

Face detected using InsightFace detection module.

![Face Detection](images/face-detection.png)

### Step 3: Generate Embedding

Buffalo model generated a 512-dimensional face embedding.

![Embedding Generation](images/testing-embedding.png)

### Step 4: Compare Against Database

Embedding compared with registered users.

![Embedding Matching](images/embedding-matching.png)

### Step 5: Display Recognition Result

User name displayed if similarity threshold exceeded.

![Recognition Output](images/recognition-output.png)

## Performance Results

- Real-time recognition achieved.
- Recognition successful for registered users.
- Unknown users classified correctly.
- Average processing time suitable for attendance monitoring.

## Conclusion

The InsightFace Buffalo ONNX model provided reliable real-time face recognition and is suitable for integration with the attendance management system.
