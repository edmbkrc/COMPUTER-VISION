import cvlib as cv
from cvlib.object_detection import draw_bbox
import cv2

webcam = cv2.VideoCapture("http://192.168.1.101:8080/video")

while webcam.isOpened():
    ret, frame = webcam.read()

    bbox, label, conf = cv.detect_common_objects(frame)

    out = draw_bbox(frame, bbox, label, conf)

    cv2.imshow("Gerçek zamanlı nesne tespiti", out)

    if cv2.waitKey(1) & 0xFF == ord("q"):
        break

webcam.release()
cv2.destroyAllWindows()





