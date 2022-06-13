from configparser import Interpolation
import cv2 as cv

### Reading images
img = cv.imread('photos/chris1.jpg')
# BGR order if you used cv2.imread()
# RGB order if you used mpimg.imread()

cv.imshow('christmas', img) # display the image in a new window


# #converting image to grayscale
# gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY) #BGR image is a tree channell, blue, grey and red image
# cv.imshow('Gray', gray)

# #Blur an image to decrease the noise
# blur = cv.GaussianBlur(img, (7,7), cv.BORDER_DEFAULT) #
# cv.imshow('Blur', blur)

# #Edge cascade
# canny = cv.Canny(img, 125, 175) #2 threshold values
# cv.imshow('edge', canny)

# #Edge cascade
# canny = cv.Canny(blur, 125, 175) #2 threshold values
# cv.imshow('edge', canny)


# #Dilating the image
# dilated = cv.dilate(canny, (7,7), iterations=3)
# cv.imshow('Dilated', dilated)

# #Eroding 
# # eroded = cv.erode(dilated, (3,3), iterations=1)
# # cv.imshow('Eroded', eroded)

# eroded = cv.erode(img, (3,3), iterations=1)
# cv.imshow('Eroded', eroded)

# # Resize
# resized = cv.resize(img, (500,500))
# cv.imshow('Resized', resized)

# #to shrink the image
# resized = cv.resize(img, (500,500), Interpolation = cv.INTER_AREA)
# #TO LARGE THE IMAGE
# resized = cv.resize(img, (500,500), Interpolation = cv.INTER_CUBIC) # slower but better
# cv.imshow('Resized', resized)

# Cropping
cropped = img[50:200, 200:400]
cv.imshow('Cropped', cropped)

cv.waitKey(0)