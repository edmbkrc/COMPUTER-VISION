import cv2
img = cv2.imread("goruntu_isleme2.png")
cv2.imshow("Normal Resim", img)

print(img.shape) # height, width, channels, opencv BGR formatı kullanır


resized_image = cv2.resize(img, (500, 250))
resized_img = cv2.resize(img, (int(img.shape[1] / 2), int(img.shape[0] / 2)))

print(f"Resized image shape: {resized_image.shape}\nResized img shape: {resized_img.shape}")

cv2.imshow("Resized image", resized_image)
cv2.imshow("YARIYA INDIRILEN RESIM", resized_img)

cv2.waitKey(0)
cv2.destroyAllWindows()