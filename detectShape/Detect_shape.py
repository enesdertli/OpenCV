from tkinter import font
from matplotlib.pyplot import pink
import numpy as np
import cv2

# read the file and make it gray
img = cv2.imread('shapes.jpeg', cv2.IMREAD_GRAYSCALE)
# convert the colors which is close to be black to black 
_, threshold = cv2.threshold(img, 150, 255, cv2.THRESH_BINARY)
# extract contours from image
contours,_ = cv2.findContours(threshold, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
font = cv2.FONT_HERSHEY_COMPLEX

for cnt in contours:
    # approach to the shape of the original
    approx = cv2.approxPolyDP(cnt, 0.02*cv2.arcLength(cnt, True), True)
    # draw the lines
    cv2.drawContours(img, [approx], 0, (0), 5)
    
    # change the array into contiguous flattened array
    x = approx.ravel()[0]
    y = approx.ravel()[1]
    
    # detect the shapes according to its approx number
    if len(approx) == 3:
        cv2.putText(img, "Triangle", (x,y), font, 1, (0))
    elif len(approx) == 4:
        cv2.putText(img, "Rectangle", (x,y), font, 1, (0))
    elif 7 < len(approx):
        cv2.putText(img, "Circle", (x,y), font, 1, (0))
    





cv2.imshow("shapes", img)
#cv2.imshow("Threshold", threshold)
cv2.waitKey(0)
cv2.destroyAllWindows()


