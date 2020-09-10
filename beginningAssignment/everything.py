#all the versions are the same as what the book says to download
import argparse
import cv2

#Chapter 1 loading images
#you will have to change the file path of the default images
ap = argparse.ArgumentParser()
#default for image1 is pepper
ap.add_argument("--image1", required = False,
    default = "/Users/nicholasliu/Documents/adhoncs/Q1tutorial/beginningAssignment/pepper.png",
    help = "Put some random image or use the default image")

images = vars(ap.parse_args())
image1 = cv2.imread(images["image1"])

cv2.imshow("Image1", image1)
cv2.waitKey()
