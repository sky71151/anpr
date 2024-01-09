import cv2
import os
import cv2 as cv2
import matplotlib.pyplot as plt
#import pytesseract
from PIL import Image
import glob
import numpy as np
import easyocr
import test2

# Create a VideoCapture object
cap = cv2.VideoCapture('images/parking.mp4')

# Check if camera opened successfully
if not cap.isOpened(): 
     print("Error opening video stream or file")

# Read until video is completed
while(cap.isOpened()):
  # Capture frame-by-frame
  ret, frame = cap.read()
  if ret == True:

     # convert frame to grayscale
     gray = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

     # read haarcascade for number plate detection
     cascade = cv2.CascadeClassifier('haarcascade_russian_plate_number.xml')

     # Detect license number plates
     plates = cascade.detectMultiScale(gray, 1.2, 5)
     print('Number of detected license plates:', len(plates))
     if len(plates) == 0:
         print('No license plates detected')
     else:
         index = 0
         # loop over all plates
         for (x,y,w,h) in plates:

             # draw bounding rectangle around the license number plate
             cv2.rectangle(frame, (x,y), (x+w, y+h), (0,255,0), 2)
             gray_plates = gray[y:y+h, x:x+w]
             normal_plate = frame[y:y+h, x:x+w]
             edges_plates = cv2.Canny(gray_plates, 100, 200)
             #color_plates = frame[y:y+h, x:x+w]
             
             #cv2.imwrite('images/Numberplate{}.jpg'.format(index), gray_plates)
             #cv2.imwrite('images/normalplate{}.jpg'.format(index), normal_plate)
             #blackhat_image = test2.blackhat_image('images/normalplate{}.jpg'.format(index))
             #index += 1
         #cv2.imwrite('images/Detected{}.jpg'.format(index), frame)
  # Break the loop
  else: 
     break

# When everything done, release the video capture object
cap.release()
print("done")

# Closes all the frames
#cv2.destroyAllWindows()