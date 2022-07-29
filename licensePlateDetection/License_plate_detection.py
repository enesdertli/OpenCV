from unicodedata import name
import cv2
from cv2 import blur
import numpy as np
import imutils
import matplotlib.pyplot as plt

img = cv2.imread("images/cars/car8.jpg")
img = cv2.resize(img,(500,500))

img_bgr = img
img_gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

#cv2.imshow("gray", img_gray)
#cv2.imshow("bgr", img_bgr)

img_blur = cv2.medianBlur(img_gray,5)
img_blur = cv2.medianBlur(img_blur,5)

#img_blur = cv2.bilateralFilter(img_gray, 11 ,17, 17)
#cv2.imshow("blur", img_blur)

median = np.median(img_blur)
low = 0.50*median
high = 1.50*median

img_canny = cv2.Canny(img_blur,low,high)
#cv2.imshow("canny", img_canny)

img_canny_dilate = cv2.dilate(img_canny, np.ones((3,3), np.uint8),iterations=1)
#cv2.imshow("canny_dilate", img_canny_dilate)



#####hadiiii

cnt = cv2.findContours(img_canny_dilate, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
cnt = cnt[0]
cnt = sorted(cnt, key=cv2.contourArea, reverse=True)[:30]

license = None

for c in cnt:
    rect = cv2.minAreaRect(c)
    (x,y),(w,h),r = rect
    
    
    if (w>h*2) or (h>w*2):
        box = cv2.boxPoints(rect)
        box = np.int64(box)

        minx = np.min(box[:,0])
        miny = np.min(box[:,1])
        maxx = np.max(box[:,0])
        maxy = np.max(box[:,1])

        may_license = img_gray[miny:maxy, minx:maxx].copy()
        cv2.imwrite("may_license.jpg", may_license)
        may_median = np.median(may_license)
        area = cv2.contourArea(c)
        extent = area / float(w*h)
        
        control1 = may_median > 84 and may_median < 165
        control2 = h < 50 and w < 150
        control3 = w < 50 and h < 150
        control4 = extent > 0.55
        control5 =  area >2000

        print(f"median:{may_median} width:{w}  heigh:{h} area:{area} extent:{extent}")
        found = False
         

        if(control1 and ((control2 or control3) and control4)):
            cv2.drawContours(img, [box], 0, (255,0,0), 2)
            license = [int(i) for i in [minx,miny,w,h]]
            plt.title("vuuuuu")
            found = True
            plt.imshow(cv2.cvtColor(img, cv2.COLOR_BGR2RGB))
            plt.show()
            
            
        else:
            print("couldnt detect")
            cv2.drawContours(img,[box],0,(0,0,255),2)
            plt.title("masmalesef")
    
        if(found):
            break


cv2.waitKey(0)
cv2.destroyAllWindows()