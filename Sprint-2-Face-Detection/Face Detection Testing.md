# Face Detection Testing

## Objective

Verify the performance of the face detection module.

## Step 1: Run Detection Program

Executed:

```bash
python src/face_detection.py
```

![Program Execution](images/program-execution.png)

## Step 2: Single Face Testing

Tested detection with one person.

![Single Face Test](images/single-face-test.png)

## Step 3: Multiple Face Testing

Tested detection with multiple people.

![Multiple Face Test](images/multiple-face-test.png)

## Step 4: Distance Testing

Checked performance at different distances.

![Distance Test](images/distance-test.png)

## Step 5: Lighting Condition Testing

Performed testing under different lighting conditions.

![Lighting Test](images/lighting-test.png)

## Observations

* Face detection worked correctly.
* Multiple faces were detected.
* Accuracy decreased in low-light conditions.

## Challenges Faced

* False positives occasionally occurred.
* Detection range depended on camera quality.

## Conclusion

The face detection module performed successfully and is ready for integration with the face recognition module.
