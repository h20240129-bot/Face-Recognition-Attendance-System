# Face Detection Requirements

## Objective

Identify the requirements for implementing face detection in the attendance monitoring system.

## Step 1: Study Existing Face Detection Methods

Researched different face detection approaches:

* Haar Cascade
* HOG (Histogram of Oriented Gradients)
* Deep Learning based detectors

![Face Detection Research](images/face-detection-study.png)

## Step 2: Compare Detection Techniques

Compared methods based on:

* Speed
* Accuracy
* Ease of implementation
* Hardware requirements

![Technique Comparison](images/face-detection-comparison.png)

## Step 3: Define System Requirements

The system should:

* Detect faces in real time.
* Support multiple faces.
* Work with standard webcams.
* Operate in classroom environments.

![Requirements Analysis](images/face-detection-requirements.png)

## Step 4: Select Initial Detection Method

Selected Haar Cascade because:

* Available in OpenCV.
* Fast execution.
* Suitable for prototype development.

![Method Selection](images/haar-selection.png)

## Conclusion

Haar Cascade was selected as the initial face detection technique for Sprint-02.
