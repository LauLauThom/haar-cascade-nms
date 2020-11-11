"""
Test script for haar-cascade with NMS.

Make sure to run it with the github repo as active directory.
"""
from haarcascade import Detector, __version__
print("haar-cascade-nms version:", __version__)

from skimage import io, img_as_ubyte # for image input and conversion
import matplotlib.pyplot as plt      # for display of results


## Step1: Load an image as 8-bit Grayscale for the detection with a cascade.
imgURL = r"https://zenodo.org/record/2650147/files/WE00049---E001--PO01--LO001--CO6--00000000_00.01.00_00.16.00%2C000.jpg"
img = io.imread(imgURL, as_gray=True)
img = img_as_ubyte(img)
#plt.axis("off")
#plt.imshow(img, cmap="gray")

haar_cascade = Detector(r'.\cascade\cascade.xml')
#print("Cascade classifier was correctly loaded : ", not haar_cascade.empty())
if haar_cascade.empty():
    raise Exception("Issue loading the cascade classifier, make sure it is in the subfolder above")


bboxes, scores = haar_cascade.detectAndFilter(img,
                                                scaleFactor = 1.1,
                                                minSize = (300, 300),
                                                maxSize = (500, 500),
                                                score_threshold = 1,
                                                overlap_threshold = 0.4,
                                                nObjects=2
                                                )
print("Detected bounding boxes (x,y,width,height)")
print(bboxes)
print(scores)



import cv2

imRGB = cv2.cvtColor(img, cv2.COLOR_GRAY2RGB)

for (x, y, w, h), confidence in zip(bboxes, scores):
    
        cv2.rectangle(imRGB,
                      (x, y),
                      (x+w, y+h),
                      color=(0, 255, 0),
                      thickness=10
                     )
        
        cv2.putText(imRGB, 
                    text="{:.2f}".format( confidence ), 
                    org=(x, y), 
                    fontFace=cv2.FONT_HERSHEY_PLAIN, 
                    thickness=10, 
                    fontScale=5, 
                    color=(255,255,0), 
                    lineType=cv2.LINE_AA) 

plt.figure(figsize = (10,10))
plt.axis("off")
plt.imshow(imRGB)