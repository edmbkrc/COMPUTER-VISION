import cv2
import matplotlib.pyplot as plt
import time

# Define the available OpenCV object trackers
opencv_object_trackers = {
    "kcf": cv2.legacy.TrackerKCF_create,
    "medianflow": cv2.legacy.TrackerMedianFlow_create,
    "mil": cv2.legacy.TrackerMIL_create,
    "csrt": cv2.legacy.TrackerCSRT_create,
    "boosting": cv2.legacy.TrackerBoosting_create,
    "tld": cv2.legacy.TrackerTLD_create,
    "mosse": cv2.legacy.TrackerMOSSE_create
}

tracker_name = "csrt"
trackers = cv2.legacy.MultiTracker_create()

video_path = "multi_tracking.mp4"
cap = cv2.VideoCapture(video_path)

fps = 30
f = 0

while True:
    #time.sleep(0.01)
    ret, frame = cap.read()
    if not ret:
        break

    (h, w) = frame.shape[:2]
    frame = cv2.resize(frame, dsize=(960, 600))

    # tracker güncelle
    success, bbox = trackers.update(frame)

    info = [("Tracker", tracker_name), ("Success", "Yes" if success else "No")]

    string_text = ""
    for(i, (k,v)) in enumerate(info):
        text = f"{k}: {v}"
        string_text += text + " "
        cv2.putText(frame, text, (10, 20 + i*20), cv2.FONT_HERSHEY_SIMPLEX, 0.6, (255, 0, 255), 2)

    for box in bbox:
        (x,y,w,h) = [int(v) for v in box]
        cv2.rectangle(frame, (x,y), (x+w, y+h), (0, 255, 0), 2)

    cv2.imshow("Tracking", frame)

    key = cv2.waitKey(1) & 0xFF
    if key == ord("s"):
        box = cv2.selectROI("Tracking", frame, False)
        if box != (0, 0, 0, 0):
            tracker = opencv_object_trackers[tracker_name]()
            trackers.add(tracker, frame, box)

    elif key == ord("q"):
        break

    f += 1

cap.release()
cv2.destroyAllWindows()




