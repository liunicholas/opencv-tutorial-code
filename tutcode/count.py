import numpy as np
import argparse
import cv2

ap = argparse.ArgumentParser()
ap.add_argument("-i", "--image", required = True,
	help = "Path to the image")
#/Users/nicholasliu/Documents/adhoncs/Q1tutorial/tutcode/rain.png
#/Users/nicholasliu/Documents/adhoncs/Q1tutorial/tutcode/coins.png
args = vars(ap.parse_args())

image = cv2.imread(args["image"])
#grayscale and gaussian blur to make edge detection easier as usual
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
blurred = cv2.GaussianBlur(gray, (11, 11), 0)
cv2.imshow("Image", image)

#tweak lower and upper bounds
#very hard
edged = cv2.Canny(blurred, 100, 250)
cv2.imshow("Edges", edged)

#parameters are edged image, type of countour, and how precise to make the counter
#returns a destroyed image, the countours, and the hierarchy of contour (doesn't matter in this one)
cnts, SOMEHTIGNG = cv2.findContours(edged.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

print(f"{len(cnts)} objects in this image")

counter = 0
for item in cnts:
    counter +=1
print(counter)

objects = image.copy()
#image, contours, index of which contours, color, and thickness
cv2.drawContours(objects, cnts, -1, (0, 0, 0), 2)
cv2.imshow("original image with contours", objects)
cv2.waitKey(0)

#enumerate is basically doing range(len())
for (i, c) in enumerate(cnts):

    #starting position and then width and height
    (x, y, w, h) = cv2.boundingRect(c)

    #crops the image using numpy array slicing so its y values first
    object = image[y:y + h, x:x + w]
    cv2.imshow(f"object {i+1}", object)
    cv2.waitKey(0)

    #same idea as above but using circle
    mask = np.zeros(image.shape[:2], dtype = "uint8")
    #finds the circle to put around the contour
    ((centerX, centerY), radius) = cv2.minEnclosingCircle(c)
    cv2.circle(mask, (int(centerX), int(centerY)), int(radius), 255, -1)
    mask = mask[y:y + h, x:x + w]
    #uses the mask (which already is the outline of the object) to get rid of background with bitwise_and
    cv2.imshow("Masked object", cv2.bitwise_and(object, object, mask = mask))
    cv2.waitKey(0)
