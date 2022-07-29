import enum
import numpy as np
import cv2
import imutils

image = cv2.imread("images/binary.jpeg")
image = cv2.pyrDown(image)
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
thresh = cv2.threshold(gray, 225, 255, cv2.THRESH_BINARY_INV)[1]

cnts = cv2.findContours(thresh.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
cnts = imutils.grab_contours(cnts)
hullImage = np.zeros(gray.shape[:2], dtype="uint8")

for (i, c) in enumerate(cnts):
    (x, y, w, h) = cv2.boundingRect(c)
    
    area = cv2.contourArea(c)
    aspectRatio = float(w) / float(h)
    extent = area / float(w*h)
    perimeter = cv2.arcLength(c, True)

    print("perimeter  " +  str(perimeter))
    print("area  "+str(area))
    print("h  "+str(h))
    print("w  "+str(w))
    
    cv2.drawContours(image, [c], -1, (240, 0, 159), 3)
    shape = ""
    
    if extent < 0.80:
        if  0.98 < aspectRatio < 1.02:
            shape = "Circle"
        elif area - (area * 5 / 100) <= (w * h / 2) <= area + (area * 5 / 100):
            shape = "Triangle"
        elif area - (area * 20 / 100) <=  5.1961 * ((perimeter / 6)**2) / 2 <= area + (area * 10 / 100):
            shape = "Hexagon"
        elif area - (area * 20 / 100) <=  (perimeter / 5) * (h/2) / 2 * 5 <= area + (area * 20 / 100):
            shape = "Pentagon"
    
    elif aspectRatio >= 0.95 and aspectRatio < 1.11:
        shape = "Square"
  
    elif aspectRatio <= 0.75:
        shape = "Rectangle"
  
    cv2.putText(image, shape, (x, y - 2), cv2.FONT_HERSHEY_SIMPLEX, 0.5,
        (0,100,140), 2)
 
    print("Contour #{}, extent={:.2f},"
        .format(i + 1, extent))


cv2.imshow("Image", image)
cv2.waitKey(0)



