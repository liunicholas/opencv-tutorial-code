#instead of print statement
from __future__ import print_function
#parse command line argumnts
import argparse
#opencv library
import cv2

#get path of image on disk
ap = argparse.ArgumentParser()
ap.add_argument("-i", "--image", required = True,
	help = "Path to the image")
args = vars(ap.parse_args())

#load image off disk, returns numpy array of image
image = cv2.imread(args["image"])
#analyse image
print("width: {} pixels".format(image.shape[1]))
print("height: {} pixels".format(image.shape[0]))
print("channels: {}".format(image.shape[2]))

#name od window, image variable
cv2.imshow("Image", image)
#any keypress will work
cv2.waitKey(0)

#change to jpg
cv2.imwrite("newimage.jpg", image)
