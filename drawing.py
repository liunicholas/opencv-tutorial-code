import numpy as np
import cv2

#300 rows, 300 colums, 3 channels
#y,x
canvas = np.zeros((300,300,3), dtype = "uint8")

#define green
green = (0, 255, 0)
cv2.line(canvas, (0, 0), (300, 300), green)
cv2.imshow("Canvas", canvas)
cv2.waitKey(0)

#last argument for thickness
red = (0, 0, 255)
cv2.line(canvas, (300, 0), (150, 150), red, 3)
cv2.imshow("Canvas", canvas)
cv2.waitKey(0)

#x,y
cv2.rectangle(canvas, (10, 30), (60, 60), green)
cv2.imshow("Canvas", canvas)
cv2.waitKey(0)

cv2.rectangle(canvas, (50, 200), (200, 225), red, 5)
cv2.imshow("Canvas", canvas)
cv2.waitKey(0)

#fill in the rectangle with -1
blue = (255, 0, 0)
cv2.rectangle(canvas, (200, 50), (225, 125), blue, -1)
cv2.imshow("Canvas", canvas)
cv2.waitKey(0)

#shape0 is the height, shape1 is the width
canvas = np.zeros((300, 300, 3), dtype = "uint8")
(centerX, centerY) = (canvas.shape[1] // 2, canvas.shape[0] // 2)
white = (255, 255, 255)

#0 to 150
for r in range(0, 175, 25):
	cv2.circle(canvas, (centerX, centerY), r, white)

cv2.imshow("Canvas", canvas)
cv2.waitKey(0)

for i in range(0, 25):
    radius = np.random.randint(5, high = 200)
    #list of three numbers, changes to list
    color = np.random.randint(0, high = 256, size = (3,)).tolist()
    #2 numbers
    pt = np.random.randint(0, high = 300, size = (2,))
    print(type(pt))
    print(pt)
    cv2.circle(canvas, tuple(pt), radius, color, -1)

cv2.imshow("Canvas", canvas)
cv2.waitKey(0)
