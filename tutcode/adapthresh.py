import numpy as np
import argparse
import cv2

ap = argparse.ArgumentParser()
ap.add_argument("-i", "--vbkijdsnje", default = "/Users/nicholasliu/Documents/adhoncs/Q1tutorial/tutcode/tree.png")
args = vars(ap.parse_args())

image = cv2.imread(args["vbkijdsnje"])
image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
blurred = cv2.GaussianBlur(image, (5, 5), 0)
cv2.imshow("Image", image)

#image, max val, find t value from mean of neighborhood pixels,
#thresh method, neighborhood size, C to fine tune T value
thresh = cv2.adaptiveThreshold(blurred, 255,
	cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY_INV, 11, 4)
cv2.imshow("Mean Thresh", thresh)

#same thing but weighted average
thresh = cv2.adaptiveThreshold(blurred, 255,
	cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 15, 3)
cv2.imshow("Gaussian Thresh", thresh)
cv2.waitKey(0)
