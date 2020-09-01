import numpy as np
import cv2

#array of zeros, 300 height, 300 width
rectangle = np.zeros((300, 300), dtype = "uint8")
#255 is white and then -1 fills it in
cv2.rectangle(rectangle, (25, 25), (275, 275), 255, -1)
cv2.imshow("Rectangle", rectangle)

circle = np.zeros((300, 300), dtype = "uint8")
cv2.circle(circle, (150, 150), 150, 255, -1)
cv2.imshow("Circle", circle)

#both pixels greater than 0
bitwiseAnd = cv2.bitwise_and(rectangle, circle)
cv2.imshow("AND", bitwiseAnd)
cv2.waitKey(0)

#either pixel is greater than 0
bitwiseOr = cv2.bitwise_or(rectangle, circle)
cv2.imshow("OR", bitwiseOr)
cv2.waitKey(0)

#either but not both are greater than 0
bitwiseXor = cv2.bitwise_xor(rectangle, circle)
cv2.imshow("XOR", bitwiseXor)
cv2.waitKey(0)

#inverts on and off pixels
bitwiseNot = cv2.bitwise_not(circle)
cv2.imshow("NOT", bitwiseNot)
cv2.waitKey(0)

bitwiseNot = cv2.bitwise_not(rectangle)
cv2.imshow("NOT", bitwiseNot)
cv2.waitKey(0)
