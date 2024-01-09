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


reader = easyocr.Reader(['en'])

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

     #frame = cv2.resize(frame, (1920, 1080))
     frame = frame[1000:1800, 400:1000]
     cv2.imwrite('images/Frame.jpg', frame)
     # convert frame to grayscale
     gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

     # read haarcascade for number plate detection
     cascade = cv2.CascadeClassifier('haarcascade_russian_plate_number.xml')

     # Detect license number plates
     plates = cascade.detectMultiScale(gray, 1.25, 4)
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
             #result = reader.readtext('blackhat_image.jpg')
             #if result:
             #   cv2.putText(frame, result[0][-2], (x,y-10), cv2.FONT_HERSHEY_SIMPLEX, 1.2, (0,255,0), 2)
         cv2.imwrite('images/Detected{}.jpg'.format(index), frame)

# Closes all the frames
#cv2.destroyAllWindows()