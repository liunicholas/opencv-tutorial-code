import numpy as np
import argparse
import cv2

ap = argparse.ArgumentParser()
ap.add_argument("-i", "--something", default = "/Users/nicholasliu/Documents/adhoncs/Q1tutorial/tutcode/tree.png")
args = vars(ap.parse_args())

image = cv2.imread(args["something"])
#grayscale because its more common and simpler
image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
cv2.imshow("Original", image)

#image and then data type of output image
#8 bit has no sign
#black to white is positive slope
#white to black is negative slope, so if its only 8 bit, those edges will be missed
lap = cv2.Laplacian(image, cv2.CV_64F)
print(lap)
cv2.imshow("Laplacian witthout abs", lap)
#honeslty not sure how the absolute value works
#ASK DR J ON TUESDAY
#ASK DR J ON TUESDAY
#ASK DR J ON TUESDAY
#ASK DR J ON TUESDAY
#ASK DR J ON TUESDAY
lap = np.uint8(np.absolute(lap))
cv2.imshow("Laplacian", lap)
cv2.waitKey(0)

#image, data type, and then derivatives
#1,0 for vertical edges
#0,1 for horizontal edges
sobelX = cv2.Sobel(image, cv2.CV_64F, 1, 0)
sobelY = cv2.Sobel(image, cv2.CV_64F, 0, 1)

#ask dr j about this
sobelX = np.uint8(np.absolute(sobelX))
sobelY = np.uint8(np.absolute(sobelY))

#or so that all whites are included
sobelCombined = cv2.bitwise_or(sobelX, sobelY)

cv2.imshow("Sobel X", sobelX)
cv2.imshow("Sobel Y", sobelY)
cv2.imshow("Sobel Combined", sobelCombined)
cv2.waitKey(0)
