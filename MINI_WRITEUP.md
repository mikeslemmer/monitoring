Usage:

python ./face.py [input file] [output file].mp4

Note:

The code assumes that the opencv git repo (git@github.com:opencv/opencv.git) is checked out at the same level as this repo. This is because it uses xml files found in that other repo.

Thoughts:

* It seems possible detection and/or speed could be improved because you generally know where the face is in the video (at the right edge).
* I'm not sure if it can pick a face out when it is very dark. I'm guessing that putting an IR light on the device would help a lot. Especially considering the color information is thrown away by the algorithm.
* Using multiple recognition algorithms didn't help all that much (and it's a lot slower). Better would be to do some kind of training for this use case to generate a custom xml that worked better. This is particularly important for people wearing sunglasses.
* The code could remove spurious detections by putting in a limit on face/eye velocity. In other words, it could use the fact that it has a video stream and not just a single image to its advantage.
* Additionally, once a face is detected, it will likely be re-detected in the same region. I'm sure this fact could be used to improve the algorithm.
* The problem is made harder by the fact that the driver's face can sometimes be half out of the frame. I'm not sure if there's a good way to fix that aside from moving the camera.
