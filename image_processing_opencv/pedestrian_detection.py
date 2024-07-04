import cv2

img_path = ["padestrian1.jpeg", "padestrian2.jpeg", "padestrian3.jpeg"]

hog = cv2.HOGDescriptor()
hog.setSVMDetector(cv2.HOGDescriptor_getDefaultPeopleDetector())

for image in img_path:
    img = cv2.imread(image)
    img = cv2.resize(img,(400,400))
    (rects, weights) = hog.detectMultiScale(img, padding=(8,8), scale=1.05)

    for (x,y,w,h) in rects:
        cv2.rectangle(img, (x,y), (x+w, y+h), (255,0,255), 2)

    cv2.imshow("Pedestrians", img)

    if cv2.waitKey(0) & 0xFF == ord("q"): break

cv2.destroyAllWindows()