import cv2 as cv
import numpy as np

img = cv.imread('photos/chris1.jpg')
cv.imshow('Chris', img)

# create a blank image with the same dimension of my image
blank = np.zeros(img.shape, dtype='uint8')
#cv.imshow('Blank', blank)

gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
#cv.imshow('GRAY', gray)

# blur = cv.GaussianBlur(gray, (5,5), cv.BORDER_DEFAULT) #
# cv.imshow('Blur', blur)

# canny = cv.Canny(img, 125, 175) #2 threshold values
# cv.imshow('edge', canny)
# contours, hierarchies = cv.findContours(canny, cv.RETR_LIST, cv.CHAIN_APPROX_NONE) #TAKES THE EDGES

ret, thresh = cv.threshold(gray, 125, 255, cv.THRESH_BINARY) # if the intensity of a pixel is below 125 it will be set to 0 --> black // if it's above 255 it'set to white
contours, hierarchies = cv.findContours(thresh, cv.RETR_LIST, cv.CHAIN_APPROX_SIMPLE) #TAKES THE EDGES

#FOR HIERARCHICAL CONTOURS RETR_TREE
#FOR EXTERNAL COUNTOURS RETR_EXTERNAL
#FOR ALL COUNTOURS OF THE IMAGE RETR_LIST

# HOW WE WANT TO APPROMIMATE THE COUNTOUR
#  CHAIN_APPROX_NONE: DOES nothing
#  CHAIN_APPROX_LINE: COMPRISSES

print(f'{len(contours)} contour(s) found!')

## To save the countours of the img to the blank image!!!!!! 
cv.drawContours(blank, contours, -1, (0,0,255), 2)
cv.imshow('Contour drawn', blank)

cv.waitKey(0)