import argparse
import cv2

ap = argparse.ArgumentParser()
ap.add_argument("-i", "--image", required = True,
	help = "Path to the image")
args = vars(ap.parse_args())

image = cv2.imread(args["image"])
cv2.imshow("Original", image)

#1 = horizontal slip from y axis
flipped = cv2.flip(image, 1)
cv2.imshow("Flipped Horizontally", flipped)

#0 = vertical flip x axis
flipped = cv2.flip(image, 0)
cv2.imshow("Flipped Vertically", flipped)

#-1 flips around both axes
flipped = cv2.flip(image, -1)
cv2.imshow("Flipped Horizontally & Vertically", flipped)
cv2.waitKey(0)
