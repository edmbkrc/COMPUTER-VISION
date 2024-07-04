import cv2
import matplotlib.pyplot as plt
import numpy as np

image = cv2.imread("WaldoBeach.jpg")

cv2.imshow("where is Waldo", image)
cv2.waitKey(0)

gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

template = cv2.imread("Waldo.jpg",0)

result = cv2.matchTemplate(gray, template, cv2.TM_CCOEFF)
minVal,maxVal,minLoc,maxLoc = cv2.minMaxLoc(result)

top_left = maxLoc
bottom_right = (top_left[0] + 50, top_left[1] + 50)
cv2.rectangle(image, top_left, bottom_right,(0,0,255),5)

cv2.imshow("Where is Waldo", image)
cv2.waitKey(0)
cv2.destroyAllWindows()
