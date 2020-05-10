# Hand-Gesture-Recognition-System
Hand gesture recognition system using image processing to automate a building

befour run the application, download the hand pose model: 
OPENPOSE_URL="http://posefs1.perception.cs.cmu.edu/OpenPose/models/"
HAND_FOLDER="hand/"

after you download put that folder in root. the folder name should be "hand"

befour run the programe, make sure those packeges are installed in your machine
python

there is a file named abcd.xml that is the trained cascade classifire.
from that detect your hand with all five fingers
hand.xml, aGest.xml both detect the hand without rasing fingers
haarcascade_frontalface_fefault.xml will detected your froent face

I YOU ARE USING PYTHON 2,
$ pip install opencv-python==3.4.4.19
$ pip install opencv-contrib-python==3.4.4.19

IF YOU ARE USING PYTHON 3

$ pip3 install opencv-python==3.4.4.19
$ pip3 install opencv-contrib-python==3.4.4.19

Then run,
FOR PYTHON 2
$ python handtracking.py

FOR PYTHON 3
$ $ python3 handtracking.py

After run the above code, your web camara will be open,

then, show your hand to the camara. camara will detect your hand and start the tracking that detected object.
