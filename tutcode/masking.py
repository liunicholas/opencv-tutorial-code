import numpy as np
import argparse
import cv2

ap = argparse.ArgumentParser()
ap.add_argument("-i", "--image", required = True,
	help = "Path to the image")
args = vars(ap.parse_args())

image = cv2.imread(args["image"])
cv2.imshow("Original", image)
# print(image.shape[0])

#mask is same size as image
mask = np.zeros(image.shape[:2], dtype = "uint8")
#get center
(cX, cY) = (image.shape[1] // 2, image.shape[0] // 2)
topLeft = (cX-75, cY-75)
bottomRight = (cX+75,cY+75)
# print(topLeft)
# print(bottomRight)
cv2.rectangle(mask, topLeft, bottomRight, 255, -1)
cv2.imshow("Mask", mask)

#only checks pixels in the white rectangle
masked = cv2.bitwise_and(image, image, mask = mask)
cv2.imshow("Mask Applied to Image", masked)
cv2.waitKey(0)

mask = np.zeros(image.shape[:2], dtype = "uint8")
#draws circle this time
cv2.circle(mask, (cX, cY), 100, 255, -1)
masked = cv2.bitwise_and(image, image, mask = mask)
cv2.imshow("Mask", mask)
cv2.imshow("Mask Applied to Image", masked)
cv2.waitKey(0)
