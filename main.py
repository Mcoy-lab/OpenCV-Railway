import cv2 as cv
import numpy as np


# 循环侵蚀
def erosion_loop(er_img, n):
    temp = er_img
    for t in range(n):
        temp = cv.erode(temp, kernel, iterations=1)
    return temp


# 循环扩张
def dilation_loop(er_img, n):
    temp = er_img
    for t in range(n):
        temp = cv.dilate(temp, kernel, iterations=1)
    return temp


img = cv.imread('image/Highway.png', cv.COLOR_BGR2GRAY)
kernel = np.ones((5, 5), np.uint8)
lower_wight = np.array([0, 0, 235])
upper_wight = np.array([180, 221, 255])
hsv = cv.cvtColor(img, cv.COLOR_BGR2HSV)
mask_wight = cv.inRange(hsv, lower_wight, upper_wight)
erosion = erosion_loop(mask_wight, 15)
dilation = dilation_loop(erosion, 16)
circles = cv.HoughCircles(dilation, cv.HOUGH_GRADIENT, 4, 150, param1=50, param2=50, minRadius=0, maxRadius=0)

try:
    circles = np.uint16(np.around(circles))
except Exception as err:
    print("未找到,ERROR:" + str(err))
    exit(0)

length = circles[0][0][2]
x = circles[0][0][0]
y = circles[0][0][1]
left_angle_x = x - length
left_angle_y = y - length
right_angle_x = x + length
right_angle_y = y + length
cv.rectangle(img, (left_angle_x, left_angle_y), (right_angle_x, right_angle_y), (0, 0, 0), 4)
cv.imshow("process", dilation)
cv.imshow("consequence", img)
cv.imwrite("image/Final_process.png", erosion)
cv.imwrite("image/Final_consequence.png", img)
cv.waitKey(0)
