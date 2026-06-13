## Step 1: Install Required Libraries

Installed required packages:

pip install insightface
pip install onnxruntime
pip install opencv-python

![Library Installation](images/library-installation.png)

## Step 2: Download Buffalo Model

Downloaded the InsightFace Buffalo model package.

Model:
- buffalo_l

![Model Download](images/model-download.png)

## Step 3: Initialize Face Recognition Model

Loaded the model using InsightFace.

Example:

app = FaceAnalysis(name="buffalo_l")
app.prepare(ctx_id=0)

![Model Initialization](images/model-initialization.png)

## Step 4: Capture Face Images

Collected images of registered users.

![Dataset Collection](images/dataset-collection.png)

## Step 5: Generate Face Embeddings

The model extracts facial embeddings from each detected face.

![Embedding Generation](images/embedding-generation.png)

## Step 6: Store Encodings

Generated embeddings were stored for future comparison.

![Embedding Storage](images/embedding-storage.png)

## Step 7: Real-Time Recognition

Live camera frames were processed and embeddings compared against stored user embeddings.

![Recognition Process](images/recognition-process.png)
