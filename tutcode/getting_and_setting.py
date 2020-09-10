#Same as ch3
import argparse
import cv2

ap = argparse.ArgumentParser()
ap.add_argument("-i", "--image", required = True,
	help = "Path to the image")
args = vars(ap.parse_args())

#load image and display
image = cv2.imread(args["image"])
cv2.imshow("Original", image)

#BLUE GREEN RED ITS REVERSED
(b, g, r) = image[0, 0]
print("Pixel at (0, 0) - Red: {}, Green: {}, Blue: {}".format(r, g, b))

#changes pixel 0,0 to be RED
#sets image in b,g,r
image[5, 100] = (0, 250, 0)
(b, g, r) = image[0, 100]
print("Pixel at (0, 0) - Red: {}, Green: {}, Blue: {}".format(r, g, b))

#takes top left corner
corner = image[0:50, 0:100]
cv2.imshow("Corner", corner)

image[0:100, 0:100] = (0, 255, 0)

cv2.imshow("Updated", image)
cv2.waitKey(0)
