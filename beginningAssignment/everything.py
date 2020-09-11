#all the versions are the same as what the book says to download
import argparse
import numpy as np
import cv2

#makes parts of pepper yellow
def chapter4(image1):
    #Chapter 4 changing pixel colors
    #get the height and width of the image
    h,w = image1.shape[:2]
    totalPixels = h*w
    #counters to find the average color
    bCounter = 0
    gCounter = 0
    rCounter = 0
    for y in range(h):
        for x in range(w):
            b,g,r = image1[h-1,w-1]
            bCounter+=b
            gCounter+=g
            rCounter+=r

    #finds the average color of the image
    avgB = bCounter/totalPixels
    avgG = gCounter/totalPixels
    avgR = rCounter/totalPixels

    print(avgB,avgG,avgR)

    #i don't want to destroy the original
    image1copy = image1.copy()
    for y in range(h):
        for x in range(w):
            b,g,r = image1copy[y-1,x-1]
            print(b,g,r)
            #if the color is close enough to the average
            if abs(b-avgB)<50 and abs(g-avgG)<50 and abs(r-avgR)<50:
                print("changed")
                #change the pixel color to yellow
                image1copy[y-1,x-1] = (0,255,255)

    cv2.imshow("yellow", image1copy)
    cv2.waitKey()

#draws a new face for pepper
def chapter5(image1):
    #define some colors
    black = (0,0,0)
    yellow = (0,255,255)

    #black circle to cover her face
    cv2.circle(image1, (623,181), 125, black, -1)

    #yellow eyes
    cv2.circle(image1, (574,164), 20, yellow, -1)
    cv2.circle(image1, (678,157), 20, yellow, -1)

    #yellow mouth
    cv2.rectangle(image1, (632, 233), (652, 240), yellow, 2)

    cv2.imshow("better pepper", image1)

    cv2.waitKey()

#what pepper looks like in australia
def chapter6(image1):
    #flips image across x axis
    flippedImg = cv2.flip(image1, 0)
    cv2.imshow("Pepper in Australia", flippedImg)
    cv2.waitKey()

def main():
    #Chapter 3 loading images
    #you will have to change the file path of the default images
    ap = argparse.ArgumentParser()
    #default for image1 is pepper
    ap.add_argument("--image1", required = False,
        default = "/Users/nicholasliu/Documents/adhoncs/Q1tutorial/beginningAssignment/pepper.png",
        help = "Put some random image or use the default image")
    #default for image1 is pepper
    ap.add_argument("--image2", required = False,
        default = "/Users/nicholasliu/Documents/adhoncs/Q1tutorial/beginningAssignment/math.png",
        help = "Put homework to convert to black and white")

    images = vars(ap.parse_args())
    # print(images)
    image1 = cv2.imread(images["image1"])
    image2 = cv2.imread(images["image2"])

    cv2.imshow("Image1", image1)
    cv2.imshow("Image2", image2)
    cv2.waitKey()

    # chapter4(image1)
    # chapter5(image1)
    # chapter6(image1)

main()
