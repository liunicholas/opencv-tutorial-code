import numpy as np
import argparse
import cv2

ap = argparse.ArgumentParser()
ap.add_argument("-i", "--something", default = "/Users/nicholasliu/Documents/adhoncs/Q1tutorial/tutcode/tree.png")
args = vars(ap.parse_args())

image = cv2.imread(args["something"])
image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
image = cv2.GaussianBlur(image, (5, 5), 0)
cv2.imshow("Blurred", image)

#values greater than 150 for gradient are considered an edge
#values less than 30 are cponsidered not edge
#in between values are determined by how well they're conncetde?
#ASK DR J
canny = cv2.Canny(image, 30, 150)
cv2.imshow("Canny", canny)
cv2.waitKey(0)

#canny uses sobel gradient first
