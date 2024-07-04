import cv2
import os
"""
file = os.listdir()
#print(file)

img_path = []

for f in file:
    if f.startswith("e"):
        img_path.append(f)
        print(img_path)

"""

img_path = ["onecat.jpeg", "twocats.jpeg", "morecats.jpeg"]

for i in img_path:
    #print(i)
    img = cv2.imread(i)
    gray_image = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    cf = cv2.CascadeClassifier("haarcascade_frontalcatface.xml")

    rect = cf.detectMultiScale(gray_image, scaleFactor=1.1, minNeighbors=2)

    for (x,y,w,h) in rect:
        cv2.rectangle(img, (x,y), (x+w, y+h), (255,0,255),3)
    cv2.imshow(i, img)

    key = cv2.waitKey(0) & 0xFF
    if key == ord("c"):
        continue
    elif key == ord("q"): break

cv2.destroyAllWindows()