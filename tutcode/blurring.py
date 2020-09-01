import numpy as np
import argparse
import cv2

ap = argparse.ArgumentParser()
ap.add_argument("-i", "--image",
	help = "Path to the image", default = "/Users/nicholasliu/Documents/adhoncs/csrepo/tutcode/tree.png")
args = vars(ap.parse_args())

image = cv2.imread(args["image"])
cv2.imshow("Original", image)

#hstack is horizontal stack
blurred = np.vstack([
    #kernels are like windows that take an average of the points in the area around it
	cv2.blur(image, (3, 3)),
	cv2.blur(image, (5, 5)),
	cv2.blur(image, (19, 19))])
cv2.imshow("blurred stuff", blurred)
cv2.waitKey(0)

#more weight towards the closer pixels so its not as blurred
#dont worry abpout the zero
blurred = np.hstack([
	cv2.GaussianBlur(image, (3, 3), 0),
	cv2.GaussianBlur(image, (5, 5), 0),
	cv2.GaussianBlur(image, (7, 7), 0)])
cv2.imshow("Gaussian", blurred)
cv2.waitKey(0)

#takes a median so that the pixel is a real pixel
#less detail but no motion blur
blurred = np.hstack([
	cv2.medianBlur(image, 3),
	cv2.medianBlur(image, 5),
	cv2.medianBlur(image, 7)])
cv2.imshow("Median", blurred)
cv2.waitKey(0)

#image, diameter of surrounding pixels, number of colors, pixels surrounding
blurred = np.hstack([
	cv2.bilateralFilter(image, 5, 21, 21),
	cv2.bilateralFilter(image, 7, 31, 31),
	cv2.bilateralFilter(image, 9, 41, 41)])
cv2.imshow("Bilateral", blurred)
cv2.waitKey(0)
