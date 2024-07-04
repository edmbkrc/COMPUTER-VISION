import numpy as np
import cv2

img = cv2.imread("goruntu_isleme2.png")
resized_image = cv2.resize(img, (800, 400))

print(f"img shape: {img.shape}\nresized_image: {resized_image.shape}")
cv2.imshow("IMG", img)
cv2.imshow("IMG2", resized_image)

#dikey absbirlestirme
dikey_birlstr = np.vstack((img,resized_image))
cv2.imshow("Dikey", dikey_birlstr)

cv2.waitKey(0)
cv2.destroyAllWindows()