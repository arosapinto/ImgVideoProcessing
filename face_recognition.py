import cv2 as cv
from cv2 import FONT_HERSHEY_COMPLEX
import numpy as np



haar_cascade = cv.CascadeClassifier('haar_face.xml')


#people = ['Ben Afflek', 'Elton John', 'Madonna', 'Blake Lively', 'Oprah']
people = ['B11', 'B13', 'B19']

features = np.load('features.npy', allow_pickle=True)
labels = np.load('labels.npy')

face_recognizer = cv.face.LBPHFaceRecognizer_create()
face_recognizer.read('face_trained.yml')

#img = cv.imread(r'C:\Users\APinto\Documents\Faces\val\Elton John\Elton_John_November_2015.jpg')
img = cv.imread(r'C:\Users\APinto\Documents\Faces\train_yale\yaleB13_P00A+005E+10.jpg')

gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)

cv.imshow('Person', gray)

#Detect the face in the image
faces_rect = haar_cascade.detectMultiScale(gray, 1.1, 4)

for (x,y,w,h) in faces_rect:
    faces_roi =  gray[y:y+h,x:x+h]  

    label, confidence = face_recognizer.predict(faces_roi)
    print(f'Label = {people[label]} with a confidence of {confidence}')

    cv.putText(img, str(people[label]), (20,20), cv.FONT_HERSHEY_COMPLEX, 1.0, (0,255,0), thickness=2)

    cv.rectangle(img, (x,y), (x+w,y+h), (0,255,0), thickness=2)

cv.imshow('Detected Face', img)


cv.waitKey(0)


