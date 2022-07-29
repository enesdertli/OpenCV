import cv2
import numpy as np

img = cv2.imread('images/shapes6light.jpeg', cv2.IMREAD_COLOR)
img = cv2.pyrDown(img) 
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
edges = cv2.Canny(gray, 10, 220)
# Detect points that form a line
lines = cv2.HoughLinesP(edges, 1, np.pi/180, 100, minLineLength=20, maxLineGap=30)

# Draw lines on the image
for line in lines:
    x1, y1, x2, y2 = line[0]
    cv2.line(img, (x1, y1), (x2, y2), (255, 0, 0), 2)
    
#print(lines)

cv2.imshow("Result Image", img)
cv2.waitKey(0)
cv2.destroyAllWindows()