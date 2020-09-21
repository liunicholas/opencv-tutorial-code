#python 3.8
#all the versions are the same as what the book says to download
import argparse
import numpy as np
import cv2
import mahotas
from multiprocessing import Pool
from concurrent.futures import ThreadPoolExecutor
from time import *

#argparse to get and save the images
def chapter3():
    #you will have to change the file path of the default images
    ap = argparse.ArgumentParser()
    #default for image1 is pepper
    ap.add_argument("--image1", required = False,
        default = "/Users/nicholasliu/Documents/adhoncs/Q1tutorial/beginningAssignment/pepper.png",
        help = "Preferably use the default image")
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

    return image1, image2

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
    white = (255,255,255)
    yellow = (0,255,255)

    imageCopy = image1.copy()

    #black circle to cover her face
    cv2.circle(imageCopy, (623,181), 125, white, -1)

    #yellow eyes
    cv2.circle(imageCopy, (574,164), 20, yellow, -1)
    cv2.circle(imageCopy, (678,157), 20, yellow, -1)

    #yellow mouth
    cv2.rectangle(imageCopy, (632, 233), (652, 240), yellow, 2)

    cv2.imshow("better pepper", imageCopy)

    cv2.waitKey()

#what pepper looks like in australia and in robot heaven
def chapter6(image1):
    imageCopy = image1.copy()
    imageCopy2 = image1.copy()

    #flips image across x axis
    flippedImg = cv2.flip(imageCopy, 0)
    cv2.imshow("Pepper in Australia", flippedImg)

    cv2.waitKey()

    #create matrix of 100s in the same dimensions as the image
    matrix = np.ones(imageCopy2.shape, dtype = "uint8") * 100
    #increase all pixels by 100
    imageCopy2 = cv2.add(imageCopy2, matrix)
    cv2.imshow("Pepper after she runs out of battery and goes to robot heaven",
        imageCopy2)

    cv2.waitKey()

#blur just pepper's face for when she testifies against her human owners
def chapter8(image1):
    imageCopy = image1.copy()
    blurredImage = cv2.blur(imageCopy, (50, 50))

    #https://stackoverflow.com/questions/52365190/blur-a-specific-part-of-an-image
    #https://numpy.org/doc/stable/reference/generated/numpy.where.html

    #create mask with the circle on pepper's face
    mask = np.zeros(imageCopy.shape[:2], dtype = "uint8")
    mask = cv2.circle(imageCopy, (623,181), 125, (255,255,255), -1)
    #where() has three parameters, if the first paramter is true,
    #the second parameter is used, and vice versa
    finalBlurred = np.where(mask==np.array([255,255,255]), blurredImage, imageCopy)
    cv2.imshow("Anonymous Pepper", finalBlurred)

    cv2.waitKey()

#theshold the homework to convert it to black and white and be more legible
def chapter9(image2):
    image2Copy = image2.copy()

    #first convert to grey scale and blur to reduce noise and make
    #edge detection better
    greyImg = cv2.cvtColor(image2Copy, cv2.COLOR_BGR2GRAY)
    #just kiding blurring makes it worse
    # slightlyBlurredImg = cv2.GaussianBlur(greyImg, (5, 5), 0)

    #gets the best threhold for the image to convert it to binary
    threshold = mahotas.thresholding.otsu(greyImg)

    img = greyImg
    #converts anything relatively dark to be black
    img[img > threshold] = 0
    #converts everything else to white
    img[img != 0] = 255

    cv2.imshow("B&W Homework", img)

    cv2.waitKey()

    #retunr the black and white image for use in the next function
    return img

#finds the edges and then crops the background of the homework using edge detection
def chapter10and11(bAwImg):

    #finds the edges in the image
    #this edge detection didnt work very well
    #too sensitive
    # edgedImg = cv2.Canny(bAwImg, 5, 250)
    # cv2.imshow("canny edge", edgedImg)

    image = bAwImg
    #image, data type, and then derivatives
    #1,0 for vertical edges
    #0,1 for horizontal edges
    #this works better for edges
    sobelX = cv2.Sobel(image, cv2.CV_64F, 1, 0)
    sobelY = cv2.Sobel(image, cv2.CV_64F, 0, 1)
    sobelX = np.uint8(np.absolute(sobelX))
    sobelY = np.uint8(np.absolute(sobelY))

    #or so that all edges are included
    comb = cv2.bitwise_or(sobelX, sobelY)
    #reverse it
    comb = cv2.bitwise_not(comb)
    cv2.imshow("edges with sobel", comb)
    cv2.waitKey()

    image = comb.copy()

    count1 = perf_counter()

    #LOOP THROUGH MANUALLY
    h,w = comb.shape[:2]

    #left edge finder
    leftCounter = 0
    leftTotal = 0
    for y in range(h):
        #try is to find the other side of an edge
        TRY = False
        #found is for confirming a find
        FOUND = False
        for x in range(w):
            #goes downwards toward the right
            color = comb[y-1,x-1]
            #if it finds a black, it will be ready to search
            if color > 240 and TRY == False and FOUND == False:
                TRY = True
                # print(x-1)
            if TRY == True and FOUND == False:
                #will search for the white part of the line to see if it is indeed an edge
                for n in range(5):
                    if x+n < w:
                        color = comb[y-1,x+n]
                        if color < 240:
                            FOUND = True
                            leftCounter += x-1
                            leftTotal += 1.0
                            break
            #once the edge is found, this loop ends
            if FOUND == True:
                continue

    leftAvg = leftCounter/leftTotal
    print(f"left bound = {leftAvg}")

    #right edge finder
    rightCounter = 0
    rightTotal = 0
    for y in range(h):
        #try is to find the other side of an edge
        TRY = False
        #found is for confirming a find
        FOUND = False
        for x in range(w):
            #goes downwards toward the left
            color = comb[y-1,w-x-1]
            #if it finds a black, it will be ready to search
            if color > 240 and TRY == False and FOUND == False:
                TRY = True
            if TRY == True and FOUND == False:
                #will search for the white part of the line to see if it is indeed an edge
                for n in range(5):
                    if x-n > 0:
                        color = comb[y-1,x-n-1]
                        if color < 240:
                            FOUND = True
                            rightCounter += w-x-1
                            rightTotal += 1.0
                            break
            #once the edge is found, this loop ends
            if FOUND == True:
                continue

    rightAvg = rightCounter/rightTotal
    print(f"right bound = {rightAvg}")

    #top edge finder
    topCounter = 0
    topTotal = 0
    for x in range(w):
        #try is to find the other side of an edge
        TRY = False
        #found is for confirming a find
        FOUND = False
        for y in range(h):
            #goes rightwards toward the bottom
            color = comb[y-1,x-1]
            #if it finds a black, it will be ready to search
            if color > 240 and TRY == False and FOUND == False:
                TRY = True
            if TRY == True and FOUND == False:
                #will search for the white part of the line to see if it is indeed an edge
                for n in range(5):
                    if y+n < h:
                        color = comb[y+n,x-1]
                        if color < 240:
                            FOUND = True
                            topCounter += y-1
                            topTotal += 1.0
                            break
            #once the edge is found, this loop ends
            if FOUND == True:
                continue

    topAvg = topCounter/topTotal
    print(f"top bound = {topAvg}")

    #bottom edge finder
    bottomCounter = 0
    bottomTotal = 0
    for x in range(w):
        #try is to find the other side of an edge
        TRY = False
        #found is for confirming a find
        FOUND = False
        for y in range(h):
            #goes rightwards toward the bottom
            color = comb[h-y-1,x-1]
            #if it finds a black, it will be ready to search
            if color > 240 and TRY == False and FOUND == False:
                TRY = True
            if TRY == True and FOUND == False:
                #will search for the white part of the line to see if it is indeed an edge
                for n in range(5):
                    if h-y-n > 0:
                        color = comb[h-y-n-1,x-1]
                        if color < 240:
                            FOUND = True
                            bottomCounter += h-y-1
                            bottomTotal += 1.0
                            break
            #once the edge is found, this loop ends
            if FOUND == True:
                continue

    bottomAvg = bottomCounter/bottomTotal
    print(f"bottom bound = {bottomAvg}")

    count2 = perf_counter()

    time = count2-count1
    print(f"total time without multiprocessing: {time}")

    #https://stackoverflow.com/questions/32404825/how-to-run-multiple-functions-at-same-time
    executors_list = []

    cs = [[comb, "top"],[comb, "bottom"],[comb, "left"],[comb, "right"]]
    with ThreadPoolExecutor(max_workers=4) as executor:
        executors_list.append(executor.submit(edgeFind, cs[0]))
        executors_list.append(executor.submit(edgeFind, cs[1]))
        executors_list.append(executor.submit(edgeFind, cs[2]))
        executors_list.append(executor.submit(edgeFind, cs[3]))

    # for x in executors_list:
    #     print(x.result())

    count3 = perf_counter()

    time = count3-count2
    print(f"total time with multithreading: {time}")

    cs = [[comb, "top"],[comb, "bottom"],[comb, "left"],[comb, "right"]]
    with Pool(processes=4, maxtasksperchild = 1) as pool:
            results = pool.map(edgeFind, cs)
            pool.close()
            pool.join()

    # print(results)

    count4 = perf_counter()

    time = count4-count3
    print(f"total time with multitprocessing: {time}")

    # cv2.imshow("cropped homework", image)
    #crops the image using the edges found
    y2 = int(bottomAvg)
    y1 = int(topAvg)
    x1 = int(leftAvg)
    x2 = int(rightAvg)
    croppedImg = image[y1:y2, x1:x2]
    cv2.imshow("cropped homework", croppedImg)

    cv2.waitKey()

def edgeFind(cs):
    comb = cs[0]
    side = cs[1]

    h,w = comb.shape[:2]

    if side=="left":
        #left edge finder
        leftCounter = 0
        leftTotal = 0
        for y in range(h):
            #try is to find the other side of an edge
            TRY = False
            #found is for confirming a find
            FOUND = False
            for x in range(w):
                #goes downwards toward the right
                color = comb[y-1,x-1]
                #if it finds a black, it will be ready to search
                if color > 240 and TRY == False and FOUND == False:
                    TRY = True
                    #print(x-1)
                if TRY == True and FOUND == False:
                    #will search for the white part of the line to see if it is indeed an edge
                    for n in range(5):
                        if x+n < w:
                            color = comb[y-1,x+n]
                            if color < 240:
                                FOUND = True
                                leftCounter += x-1
                                leftTotal += 1.0
                                break
                #once the edge is found, this loop ends
                if FOUND == True:
                    continue

        leftAvg = leftCounter/leftTotal
        print(f"left bound = {leftAvg}")

        return leftAvg

    if side=="right":
        #right edge finder
        rightCounter = 0
        rightTotal = 0
        for y in range(h):
            #try is to find the other side of an edge
            TRY = False
            #found is for confirming a find
            FOUND = False
            for x in range(w):
                #goes downwards toward the left
                color = comb[y-1,w-x-1]
                #if it finds a black, it will be ready to search
                if color > 240 and TRY == False and FOUND == False:
                    TRY = True
                if TRY == True and FOUND == False:
                    #will search for the white part of the line to see if it is indeed an edge
                    for n in range(5):
                        if x-n > 0:
                            color = comb[y-1,x-n-1]
                            if color < 240:
                                FOUND = True
                                rightCounter += w-x-1
                                rightTotal += 1.0
                                break
                #once the edge is found, this loop ends
                if FOUND == True:
                    continue

        rightAvg = rightCounter/rightTotal
        print(f"right bound = {rightAvg}")

        return rightAvg

    if side=="top":
        #top edge finder
        topCounter = 0
        topTotal = 0
        for x in range(w):
            #try is to find the other side of an edge
            TRY = False
            #found is for confirming a find
            FOUND = False
            for y in range(h):
                #goes rightwards toward the bottom
                color = comb[y-1,x-1]
                #if it finds a black, it will be ready to search
                if color > 240 and TRY == False and FOUND == False:
                    TRY = True
                if TRY == True and FOUND == False:
                    #will search for the white part of the line to see if it is indeed an edge
                    for n in range(5):
                        if y+n < h:
                            color = comb[y+n,x-1]
                            if color < 240:
                                FOUND = True
                                topCounter += y-1
                                topTotal += 1.0
                                break
                #once the edge is found, this loop ends
                if FOUND == True:
                    continue

        topAvg = topCounter/topTotal
        print(f"top bound = {topAvg}")

        return topAvg

    if side=="bottom":
        #bottom edge finder
        bottomCounter = 0
        bottomTotal = 0
        for x in range(w):
            #try is to find the other side of an edge
            TRY = False
            #found is for confirming a find
            FOUND = False
            for y in range(h):
                #goes rightwards toward the bottom
                color = comb[h-y-1,x-1]
                #if it finds a black, it will be ready to search
                if color > 240 and TRY == False and FOUND == False:
                    TRY = True
                if TRY == True and FOUND == False:
                    #will search for the white part of the line to see if it is indeed an edge
                    for n in range(5):
                        if h-y-n > 0:
                            color = comb[h-y-n-1,x-1]
                            if color < 240:
                                FOUND = True
                                bottomCounter += h-y-1
                                bottomTotal += 1.0
                                break
                #once the edge is found, this loop ends
                if FOUND == True:
                    continue

        bottomAvg = bottomCounter/bottomTotal
        print(f"bottom bound = {bottomAvg}")

        return bottomAvg

def main():

    image1, image2 = chapter3()
    chapter4(image1)
    chapter5(image1)
    chapter6(image1)
    chapter8(image1)
    bAwImg = chapter9(image2)
    chapter10and11(bAwImg)

#must use this for multitprocessing
if __name__ == '__main__':
	main()
