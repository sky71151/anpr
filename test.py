import os
import cv2 as cv2
import matplotlib.pyplot as plt
import pytesseract
from PIL import Image
import glob
import numpy as np
import easyocr
#from paddleocr import PaddleOCR, draw_ocr
#ocr = PaddleOCR(use_angle_cls=True, lang="en") # need to run only once to download and load model into memory


reader = easyocr.Reader(['en'])

# Read input image
img = cv2.imread("belgische.jpg")
#img = cv2.imread("verkeer.jpg")  
#img = cv2.imread("bmw.jpg")

# convert input image to grayscale
gray = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

# read haarcascade for number plate detection
cascade = cv2.CascadeClassifier('haarcascade_russian_plate_number.xml')

# Detect license number plates
plates = cascade.detectMultiScale(gray, 1.2, 5)
print('Number of detected license plates:', len(plates))
if len(plates) == 0:
   print('No license plates detected')
   exit(0)
else:
   index = 0
   # loop over all plates
   for (x,y,w,h) in plates:
   
      # draw bounding rectangle around the license number plate
      cv2.rectangle(img, (x,y), (x+w, y+h), (0,255,0), 2)
      gray_plates = gray[y:y+h, x:x+w]
      edges_plates = cv2.Canny(gray_plates, 100, 200)
      color_plates = img[y:y+h, x:x+w]
      cv2.imwrite('Detected{}.jpg'.format(index), img)
      cv2.imwrite('Numberplate{}.jpg'.format(index), gray_plates)
   
   # save number plate detected
   sigma = 0.5  # Assign a value to sigma if needed

   #cv2.imshow('Number Plate', gray_plates)
   #cv2.imshow('Number Plate Edges', edges_plates)

   median = np.median(gray_plates)
   lower = int(max(0, (1.0 - sigma) * median))
   upper = int(min(255, (1.0 + sigma) * median))

   edge_image= cv2.Canny(gray_plates, 0.3, 100)
   cv2.imwrite('edge_images.jpg', edge_image)
   cv2.imwrite('plateEdges.jpg', edges_plates)
   text = pytesseract.image_to_string(Image.open('Numberplate.jpg'))
   result = reader.readtext('Numberplate.jpg')
   #result2 = ocr.ocr('Numberplate.jpg')
   print(result)
   #print(result2)
   print(text)
   print ('test')
   #cv2.imshow('Number Plate Image', img)
   
   #cv2.waitKey(0)
   #cv2.destroyAllWindows()