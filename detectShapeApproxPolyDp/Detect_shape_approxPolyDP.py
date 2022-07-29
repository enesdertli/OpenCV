import cv2
from cv2 import THRESH_BINARY
import numpy as np

input_image = cv2.imread("images/shapes_more.jpeg")

######### Smaller
input_image = cv2.pyrDown(input_image)

#input_image = cv2.GaussianBlur(input_image,(7,7),2)
input_image = cv2.blur(input_image, (5,5))

input_image_copy = input_image.copy()

######### First we need to convert it into gray
gray_img = cv2.cvtColor(input_image, cv2.COLOR_BGR2GRAY)

######### I chose the whitest point for threshold to get better result but didn't used
threshold_value = gray_img[448,169]
#print(threshold_value)

######### Now our shapes are black color and background is white color.
ret, binary_img = cv2.threshold(gray_img, 155, 255, cv2.THRESH_BINARY)

######### Opposite of the binary_image, so now we have shapes which is white color, and background which is black color.
inverted_binary_img = ~ binary_img

cv2.imshow("binary",binary_img)
cv2.imshow("inverted_binary_img",inverted_binary_img)
#cv2.imwrite("corner.jpeg", binary_img)

######### We used chain_approx_simple method because we just need end points, not all of the points on the line. Also retr_tree is more suitable to others
contours_list, hierarchy = cv2.findContours(inverted_binary_img, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)


for contour_num in range(len(contours_list)):

    ######### To draw the contour lines on the image. src, contours all we have, ıd of the contour, color, thickness
    output = cv2.drawContours(input_image_copy,contours_list, contour_num, (255, 0, 255), 3)

    ######### The approxPolyDP() function uses the Douglas Peucker algorithm to approximate the contour shape to another shape. It is an algorithm that decimates a curve composed of line segments to a similar curve with fewer points according to ε. The smaller ε means more points. So if we give smaller ε, our new shapes would be more smooth as we want.
    end_points = cv2.approxPolyDP(contours_list[contour_num], 0.01 * cv2.arcLength(contours_list[contour_num], True), True)
    
    ######### It finds area of the shape
    if(cv2.contourArea(contours_list[contour_num])) > 10000:

        point_x = end_points[0][0][0]
        point_y = end_points[0][0][1]
        text_color = (0,0,0)

        if len(end_points) == 3:
            cv2.putText(input_image_copy, 'Triangle', (point_x, point_y),
                        cv2.FONT_HERSHEY_SIMPLEX, 0.9, text_color, 2)
 
        elif len(end_points) == 4:
            ######### If we have 4 end points, shapes might be square or rectangle. To find this we can calculate the ratio of the edges. If ratio is close to 1, shape is probably a square. If ratio is not close to 1, shape is probably a rectangle.
            x, y, w, h = cv2.boundingRect(end_points)
            aspectRatio = float(w)/h
            #print(aspectRatio)

            if aspectRatio >= 0.95 and aspectRatio < 1.15:
                cv2.putText(input_image_copy, 'Square', (point_x, point_y),
                cv2.FONT_HERSHEY_SIMPLEX, 0.9, text_color, 2)
            else:
                cv2.putText(input_image_copy, 'Rectangle', (point_x, point_y),
                cv2.FONT_HERSHEY_SIMPLEX, 0.9, text_color, 2)
 
        elif len(end_points) == 5:
            cv2.putText(input_image_copy, 'Pentagon', (point_x, point_y),
                        cv2.FONT_HERSHEY_SIMPLEX, 0.9, text_color, 2)

        elif len(end_points) == 6:
            cv2.putText(input_image_copy, 'Hexagon', (point_x, point_y),
                        cv2.FONT_HERSHEY_SIMPLEX, 0.9, text_color, 2)
 
        else:
            cv2.putText(input_image_copy, 'Circle', (point_x, point_y),
                        cv2.FONT_HERSHEY_SIMPLEX, 0.9, text_color, 2)

#cv2.imwrite("output.jpeg", output)
cv2.imshow("shapes",output)
cv2.waitKey(0)
cv2.destroyAllWindows()