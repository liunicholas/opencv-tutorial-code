import numpy as np
import argparse
import cv2

ap = argparse.ArgumentParser()
ap.add_argument("-i", "--image", required = True,
	help = "Path to the image")
args = vars(ap.parse_args())

image = cv2.imread(args["image"])
cv2.imshow("Original", image)

#y values and then x values because this is nmumpy array
cropped = image[30:120 , 240:335]
cv2.imshow("cropped", cropped)
cv2.waitKey(0)
