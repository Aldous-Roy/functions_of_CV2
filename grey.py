import cv2 as cv
import numpy as np

img=cv.imread("./photos/cat.jpeg")
cv.imshow("normal",img)

#grey-scale
gray=cv.cvtColor(img,cv.COLOR_BGR2GRAY)
cv.imshow("gray-scale",gray)

#Gaussian Blur
blur=cv.GaussianBlur(img,(15,15),2)
cv.imshow("blurring",blur)

#edges
edges=cv.Canny(blur,125,175)
cv.imshow("edges",edges)

#Dialated
dai=cv.dilate(img,(3,3),iterations=8)
cv.imshow("dialated",dai)

#eroding
erode=cv.erode(img,(5,5),iterations=5)
cv.imshow("eroding",erode)

#resize
resize=cv.resize(img,(100,100))
cv.imshow("Resized",resize)

cv.waitKey(0)