import cv2
import sys

params = sys.argv
inputName = params[1]
outputname = params[2]

image = cv2.imread(inputName)
mask = cv2.imread("tex_0000_mask.png")
src = cv2.imread("tex_0000_clean.png")

ears = cv2.bitwise_and(src, mask)
face = cv2.bitwise_and(image, cv2.bitwise_not(mask))
result = cv2.bitwise_or(ears, face)

cv2.imwrite(outputname, result)