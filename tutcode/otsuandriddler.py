import numpy as np
import argparse
import mahotas
import cv2

ap = argparse.ArgumentParser()
ap.add_argument("-i", "--vbkijdsnje", default = "/Users/nicholasliu/Documents/adhoncs/Q1tutorial/tutcode/tree.png")
#its a dictionary
args = vars(ap.parse_args())

image = cv2.imread(args["vbkijdsnje"])
image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
blurred = cv2.GaussianBlur(image, (5, 5), 0)
cv2.imshow("Image", image)

#this method finds the T value for us
T = mahotas.thresholding.otsu(blurred)
print("Otsu's threshold: {}".format(T))

thresh = image.copy()
#any pixel more than T becomes white
thresh[thresh > T] = 255
#any other pixel becomes black
thresh[thresh < 255] = 0
#inverts the colors
thresh = cv2.bitwise_not(thresh)
cv2.imshow("Otsu", thresh)

#same thing but with riddler calvard method
T = mahotas.thresholding.rc(blurred)
print("Riddler-Calvard: {}".format(T))
thresh = image.copy()
thresh[thresh > T] = 255
thresh[thresh < 255] = 0
thresh = cv2.bitwise_not(thresh)
cv2.imshow("Riddler-Calvard", thresh)
cv2.waitKey(0)
