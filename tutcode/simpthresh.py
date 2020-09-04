import numpy as np
import argparse
import cv2

ap = argparse.ArgumentParser()
ap.add_argument("-i", "--vbkijdsnje", default = "/Users/nicholasliu/Documents/adhoncs/Q1tutorial/tutcode/tree.png")
args = vars(ap.parse_args())

image = cv2.imread(args["vbkijdsnje"])
#convert to grayscale
image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
blurred = cv2.GaussianBlur(image, (5, 5), 0)
cv2.imshow("Original", image)

#grayscale image, t threshhold, intensity of pixels above (white), and method
#returns value of threshold and the image
#inveresed so dark becomes white and white becomes dark
(T, threshInv) = cv2.threshold(blurred, 210, 255, cv2.THRESH_BINARY_INV)
cv2.imshow("Threshold Binary Inverse", threshInv)

#this is the normal one
(T, thresh) = cv2.threshold(blurred, 230, 255, cv2.THRESH_BINARY)
cv2.imshow("Threshold Binary", thresh)

#not great image to use, too much white around the image
cv2.imshow("clouds", cv2.bitwise_and(image, image, mask = thresh))
cv2.waitKey(0)
