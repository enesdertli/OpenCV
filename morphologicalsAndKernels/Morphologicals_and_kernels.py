import cv2
from matplotlib import pyplot as plt
import numpy as np
# reading the file and converting it into gray
img = cv2.imread("images/smarties.png", cv2.IMREAD_GRAYSCALE)

_, mask = cv2.threshold(img, 220, 255, cv2.THRESH_BINARY_INV)

kernal = np.ones((2,2), np.uint8)

dilation = cv2.dilate(mask, kernal, iterations=2)
erosion = cv2.erode(mask, kernal, iterations=1)
opening = cv2.morphologyEx(mask, cv2.MORPH_OPEN, kernal)
closing = cv2.morphologyEx(mask, cv2.MORPH_CLOSE, kernal)
mg = cv2.morphologyEx(mask, cv2.MORPH_GRADIENT, kernal)
th = cv2.morphologyEx(mask, cv2.MORPH_TOPHAT, kernal)

#
multipleimg_row1= np.concatenate((dilation,erosion,opening),axis=1)
multipleimg_row2= np.concatenate((closing,mg,th),axis=1)
multipleimg_total= np.concatenate((multipleimg_row1,multipleimg_row2),axis=0)

cv2.imshow("smarties",multipleimg_total)
cv2.waitKey(0)
cv2.destroyAllWindows()

