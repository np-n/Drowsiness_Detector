### Drowsiness Detector

Drowsiness detection is a safety technology that can prevent accidents that are caused by drivers who fell asleep while driving.

Drowsiness can be identified by using vision-based techniques like eyes detection, yawning, and nodding.

This detection system identifies key attributes of drowsiness and triggers an alarm when someone is drowsy.


To run the detector,at first install the requirements in virtual environment

`pip install -r requirements.txt`

Download the dlib face landmark detector from http://dlib.net/files/shape_predictor_68_face_landmarks.dat.bz2 . and extract .dat file and move it to `resources/model/` in root directory.
Download the alarm music from internet and place it on `resources/music/`.

after successfully installing and downloading requirements run `drowsiness_detector`.

`python drowsiness_detector.py`