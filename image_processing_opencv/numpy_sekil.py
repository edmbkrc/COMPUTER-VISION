import cv2
import numpy as np

img = cv2.imread("goruntu_isleme2.png")
cv2.imshow("Normal Resim",img)

print(img.shape)

img_resized = cv2.resize(img,(500,300))
cv2.imshow("Resized IMG", img_resized)

cropped_image = img[100:300,200:600]
print("cropped image shape: ",cropped_image.shape)
cv2.imshow("CROPPED IMAGE", cropped_image)

cv2.waitKey(0)
cv2.destroyAllWindows()