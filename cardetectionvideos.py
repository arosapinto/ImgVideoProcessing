""""1. Apply frame differencing on every pair of consecutive frames
    2. Apply image thresholding on the output image of the previous step
    3. Perform image dilation on the output image of the previous step
    4. Find contours in the output image of the previous step
    5. Shortlist contours appearing in the detection zone
    6. Save frames along with the final contours"""


import os
import re
import cv2 # opencv library
import numpy as np
from os.path import isfile, join
import matplotlib.pyplot as plt


vidcap = cv2.VideoCapture('C:\\Test folder\\images\\videos\\slow_traffic_small.mp4')

count = 0
while vidcap.isOpened():   
  ret, image = vidcap.read()
  if ret == False:
      break
  if count%20 == 0:  
    cv2.imwrite('C:\\Test folder\\images\\videos\\frames\\car_frames\\new'+str(count)+'.jpg', image)     # save frame as JPEG file   
  count += 1

vidcap.release()
#cv2.destroyAllWindows()



# get file names of the frames
col_frames = os.listdir('C:/Test folder/images/videos/frames/car_frames/')

# sort file names
col_frames.sort(key=lambda f: int(re.sub('\D', '', f)))

# empty list to store the frames
col_images=[]

for i in col_frames:
    # read the frames
    img = cv2.imread('C:/Test folder/images/videos/frames/car_frames/'+i)
    # append the frames to the list
    col_images.append(img)

# plot 25th frame
i = 25
for frame in [i, i+1]:
    plt.imshow(cv2.cvtColor(col_images[frame], cv2.COLOR_BGR2RGB))
    plt.title("frame: "+str(frame))
    plt.show()

##########################################################

# kernel for image dilation
kernel = np.ones((4,4),np.uint8)

# font style
font = cv2.FONT_HERSHEY_SIMPLEX

# directory to save the ouput frames
pathIn = "C:/Test folder/images/videos/frames/car_frames/"

for i in range(len(col_images)-1):
    
    # frame differencing
    grayA = cv2.cvtColor(col_images[i], cv2.COLOR_BGR2GRAY)
    grayB = cv2.cvtColor(col_images[i+1], cv2.COLOR_BGR2GRAY)
    diff_image = cv2.absdiff(grayB, grayA)
    
    # image thresholding
    ret, thresh = cv2.threshold(diff_image, 30, 255, cv2.THRESH_BINARY)
    
    # image dilation
    dilated = cv2.dilate(thresh,kernel,iterations = 1)
    
    # find contours
    contours, hierarchy = cv2.findContours(dilated.copy(), cv2.RETR_TREE,cv2.CHAIN_APPROX_NONE)
    
    # shortlist contours appearing in the detection zone
    valid_cntrs = []
    for cntr in contours:
        x,y,w,h = cv2.boundingRect(cntr)
        if (x > 300) & (y >= 200) & (cv2.contourArea(cntr) >= 550):
            # if (y >= 350) & (cv2.contourArea(cntr) < 500):
            #     break
            valid_cntrs.append(cntr)
            
        
    # add contours to original frames
    dmy = col_images[i].copy()
    cv2.drawContours(dmy, valid_cntrs, -1, (127,200,0), 2)
    
    cv2.putText(dmy, "vehicles detected: " + str(len(valid_cntrs)), (55, 15), font, 0.6, (0, 180, 0), 2)
    cv2.line(dmy, (0, 150), (650,150), (100, 650, 650))
    cv2.imwrite(pathIn+str(i)+'.png',dmy)  


    # specify video name
pathOut = 'C:\Test folder\images\videos\slow_traffic_small.mp4'

# specify frames per second
fps = 14.0

frame_array = []
files = [f for f in os.listdir(pathIn) if isfile(join(pathIn, f))]


files.sort(key=lambda f: int(re.sub('\D', '', f)))

for i in range(len(files)):
    filename=pathIn + files[i]
    
    #read frames
    img = cv2.imread(filename)
    height, width, layers = img.shape
    size = (width,height)
    
    #inserting the frames into an image array
    frame_array.append(img)


out = cv2.VideoWriter(pathOut,cv2.VideoWriter_fourcc(*'mp4v'), fps, size)

for i in range(len(frame_array)):
    # writing to a image array
    out.write(frame_array[i])

out.release()