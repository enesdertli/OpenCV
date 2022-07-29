import cv2
from cv2 import dilate
import numpy as np
import imutils
import matplotlib.pyplot as plt

img = cv2.imread("may_license.jpg",1)
img_output = cv2.imread("may_license.jpg",1)
img = cv2.resize(img,(240,180))
img_output = cv2.resize(img,(240,180))


###########################
img_bilateral = cv2.bilateralFilter(img.copy(),15,75,75)

def autoCanny(img, sigma=0.33):
    median = np.median(img)
    lower = int(max(0,(1-sigma)*median))
    upper = int(min(255,(1+sigma)*median))
    canny = cv2.Canny(img,lower,upper)
    return canny
img_canny = autoCanny(img_bilateral)

contours_list, hierarchy = cv2.findContours(img_canny, cv2.RETR_TREE, cv2.CHAIN_APPROX_NONE)
contours_list = sorted(contours_list, key=cv2.contourArea, reverse=True)[:15]


for contour_num in range(len(contours_list)):

    output = cv2.drawContours(img_output,contours_list, contour_num, (255, 255, 255), 2)

for (i, c) in enumerate(contours_list):
    rect = cv2.boundingRect(c)
    x, y, w, h = rect
    box = cv2.rectangle(img, (x,y), (x+w, y+h), (0,0,255), 1)
    cropped = img[(y-8): (y+h+8), x: x+w] 
    #cv2.imshow("boxes", cropped)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
    cv2.imwrite("blobby" + str(i)+".png", cropped), 

###########################

cv2.imshow("img", img)
cv2.imshow("bilateral", img_bilateral)
cv2.imshow("canny", img_canny)
cv2.imshow("contours", output)
#cv2.imwrite("filter.jpg", img_bilateral)
cv2.waitKey(0)
cv2.destroyAllWindows()


