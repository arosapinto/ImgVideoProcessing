import cv2 as cv
import numpy as np


## we can create a dummy image or draw in the original one
blank = np.zeros((500,500,3), dtype='uint8') # 3 is the number of colour channel, 500 is thw widht and height
cv.imshow('BLANK', blank)


#1. PAINT THE IMAGE A CERTAIN COLOUR
# blank[:] = 0,255,0 #: means all the pixels
# cv.imshow('Green', blank)


# # range of pixels
# blank[200:300, 300:400] = 0,0,255 #colour red
# cv.imshow('Green', blank)

# # 2. DRAW a Rectangule
# cv.rectangle(blank, (0,0), (250,250), (0,255,0), thickness=2) # origin and end of the rectangule, colour and the thickness of the line
# cv.imshow('rectangle', blank)

### to have a filled rectangle
# cv.rectangle(blank, (0,0), (250,250), (0,255,0), thickness=cv.FILLED) # origin and end of the rectangule, colour and the thickness of the line
# cv.imshow('filled rectangle', blank)

###to have the rectangule scaled to half of the original image
# cv.rectangle(blank, (0,0), (blank.shape[1]//2, blank.shape[0]//2), (0,255,0), thickness=-1) # origin and end of the rectangule, colour and the thickness of the line
# cv.imshow('filled rectangle', blank)


# # 3. DRAW A CIRCLE
# cv.circle(blank, (blank.shape[1]//2, blank.shape[0]//2), 40, (0,0,255), thickness=3) # coordenates of the center, radius of 40 pixels
# cv.imshow('circle', blank)


# # 4. DRAW A LINE
# cv.line(blank, (0,0), (blank.shape[1]//2, blank.shape[0]//2), (255,255,255), thickness=3) # draws the line between the two points we select
# cv.imshow('line', blank)

# 5. Write text
cv.putText(blank, 'How are you?', (10,225), cv.FONT_HERSHEY_TRIPLEX, 1.0, (0,255,0), 2) #origin where we want the text, 1.0 is the font size, colour ant thickness
cv.imshow('text', blank)

cv.waitKey(0)



