import cv2
import numpy as np

img = cv2.imread("images/shapes6light.jpeg")
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
blur = cv2.GaussianBlur(gray,(3,3),0)
blur = cv2.pyrDown(blur)    


def autoCanny(blur, sigma=0.33):
    median = np.median(blur)
    lower = int(max(0,(1-sigma)*median))
    upper = int(min(255,(1+sigma)*median))
    canny = cv2.Canny(blur,lower,upper)
    return canny

wide = cv2.Canny(blur,10,220)
tight = cv2.Canny(blur,200,230)
auto = autoCanny(blur)

cv2.imshow("edges", np.hstack([wide,auto]))
#cv2.imshow("aa",tight)
cv2.waitKey(0)
cv2.destroyAllWindows()
