"""Background subtraction (BS) is a common and widely used technique for generating a foreground mask (namely, a binary image containing the pixels 
belonging to moving objects in the scene) by using static cameras.
As the name suggests, BS calculates the foreground mask performing a subtraction between the current frame and a background model, 
containing the static part of the scene or, more in general, everything that can be considered as background given the characteristics of the observed scene."""

from __future__ import print_function
import cv2 as cv
import argparse


parser = argparse.ArgumentParser(description='This program shows how to use background subtraction methods provided by \
                                              OpenCV. You can process both videos and images.')
parser.add_argument('--input', type=str, help='Path to a video or a sequence of image.', default='C:\\Test folder\\images\\videos\\VID-20220524-WA0001.mp4')
parser.add_argument('--algo', type=str, help='Background subtraction method (KNN, MOG2).', default='MOG2')
args = parser.parse_args()


#create Background Subtractor objects
# """ A cv::BackgroundSubtractor object will be used to generate the foreground mask. In this example, default parameters are used
# """

if args.algo == 'MOG2':
    backSub = cv.createBackgroundSubtractorMOG2()
else:
    backSub = cv.createBackgroundSubtractorKNN()

# A cv::VideoCapture object is used to read the input video or input images sequence.
capture = cv.VideoCapture(cv.samples.findFileOrKeep(args.input))
if not capture.isOpened():
    print('Unable to open: ' + args.input)
    exit(0)
while True:
    ret, frame = capture.read()
    if frame is None:
        break
 
#update the background model
# """Every frame is used both for calculating the foreground mask and for updating the background. 
#  If you want to change the learning rate used for updating the background model, it is possible to set a specific 
#  learning rate by passing a parameter to the apply method.
#  """   
    fgMask = backSub.apply(frame)

#get the frame number and write it on the current frame 
 # """The current frame number can be extracted from the cv::VideoCapture object and stamped in the top left corner of the current frame. A white rectangle is used to highlight the black colored frame number.""""   
    cv.rectangle(frame, (10, 2), (100,20), (255,255,255), -1)
    cv.putText(frame, str(capture.get(cv.CAP_PROP_POS_FRAMES)), (15, 15),
               cv.FONT_HERSHEY_SIMPLEX, 0.5 , (0,0,0))
    
    
    cv.imshow('Frame', frame)
    cv.imshow('FG Mask', fgMask)
    
    keyboard = cv.waitKey(30)
    if keyboard == 'q' or keyboard == 27:
        break