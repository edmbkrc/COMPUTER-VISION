import cv2
import numpy as np


def show_coordinates(event, x, y, flags, param):
    if event == cv2.EVENT_LBUTTONDOWN:
        print(f"Coordinates: ({x}, {y})")

phone = cv2.imread("phone.png")


cv2.namedWindow("Phone")
cv2.setMouseCallback("Phone", show_coordinates)


cv2.imshow("Phone", phone)


cv2.waitKey(0)
cv2.destroyAllWindows()
