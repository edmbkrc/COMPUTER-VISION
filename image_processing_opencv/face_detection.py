import cv2
import matplotlib.pyplot as plt
"""
einstein = cv2.imread("einstein.jpeg",0)
plt.imshow(einstein, cmap="gray")
plt.show()

face_cascade = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")

face_rect = face_cascade.detectMultiScale(einstein)

for (x,y,w,h) in face_rect:
    cv2.rectangle(einstein, (x,y),(x+w,y+h),(255,0,255),3)

plt.imshow(einstein, cmap="gray")
plt.show()


futbol = cv2.imread("futbol2.jpeg", 0)
plt.imshow(futbol, cmap = "gray")
plt.show()

face_cascade = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")

face_rect = face_cascade.detectMultiScale(futbol, minNeighbors=7)

for (x,y,w,h) in face_rect:
    cv2.rectangle(futbol, (x,y),(x+w,y+h),(255,0,255),2)

plt.imshow(futbol, cmap="gray")
plt.show()
"""
face_cascade = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")

cap = cv2.VideoCapture(0)

while True:
    ret, frame = cap.read()
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    face_rect = face_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=4)

    for (x,y,w,h) in face_rect:
        cv2.rectangle(gray, (x,y),(x+w,y+h),(255,0,255),3)

    cv2.imshow("FACE DETECTION",gray)

    if cv2.waitKey(1) & 0XFF == ord("q"):
        break

cap.release()
cv2.destroyAllWindows()