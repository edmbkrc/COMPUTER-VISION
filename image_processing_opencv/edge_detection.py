import cv2
import matplotlib.pyplot as plt
import numpy as np

image = cv2.imread("galata.png",0)
plt.figure(figsize=(8,5))
plt.imshow(image, cmap="gray")
plt.show()

#edge detection

edge = cv2.Canny(image, threshold1 = 0, threshold2 = 255)
plt.figure(figsize=(8,5))
plt.imshow(edge, cmap="gray")
plt.show()

edge = cv2.Canny(image, threshold1 = 0, threshold2 = 100)
plt.figure(figsize=(8,5))
plt.imshow(edge, cmap="gray")
plt.show()

edge = cv2.Canny(image, threshold1 = 155, threshold2 = 255)
plt.figure(figsize=(8,5))
plt.imshow(edge, cmap="gray")
plt.show()

median_value = np.median(image)
print(median_value)
low = int(max(0,(1-0.33)*median_value))
print(low)
high = int(min(255,(1+0.33)*median_value))
print(high)

edge = cv2.Canny(image, threshold1 = low, threshold2 = high)
plt.figure(figsize=(8,5))
plt.imshow(edge, cmap="gray")
plt.show()

# blurrring
blurred_image = cv2.blur(image, (5,5))
plt.figure(figsize=(8,5))
plt.imshow(blurred_image, cmap="gray")
plt.show()

edge = cv2.Canny(blurred_image, threshold1 = low, threshold2 = high)
plt.figure(figsize=(8,5))
plt.imshow(edge, cmap="gray")
plt.show()

# median blurring
blurred_image2 = cv2.medianBlur(image, ksize=5)
plt.figure(figsize=(8,5))
plt.imshow(blurred_image2, cmap="gray")
plt.show()

edge = cv2.Canny(blurred_image2, threshold1 = low, threshold2 = high)
plt.figure(figsize=(8,5))
plt.imshow(edge, cmap="gray")
plt.show()

# Gaussian blurring
blurred_image3 = cv2.GaussianBlur(image, (5,5),0)
plt.figure(figsize=(8,5))
plt.imshow(blurred_image3, cmap="gray")
plt.show()


