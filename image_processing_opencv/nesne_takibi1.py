"""
from pytube import YouTube

# Paste your YouTube video URL here
url = "https://www.youtube.com/shorts/OK0YhF3NMpQ"

# Create a YouTube object
yt = YouTube(url)

# Get the highest resolution stream
stream = yt.streams.get_highest_resolution()

# Download the video
stream.download(filename="sam_altman.mp4")

print("Video downloaded successfully!")
"""
import cv2
import matplotlib.pyplot as plt
import time

opencv_object_trackers = {
    "kcf": cv2.TrackerKCF_create,
    "medianflow": cv2.legacy.TrackerMedianFlow_create,
    "mil": cv2.TrackerMIL_create,
    "csrt": cv2.TrackerCSRT_create,
    "boosting": cv2.legacy.TrackerBoosting_create,
    "tld": cv2.legacy.TrackerTLD_create,
    "mosse": cv2.legacy.TrackerMOSSE_create
}

tracker_name = "medianflow"
tracker = opencv_object_trackers[tracker_name]()

video_path = "sam_altman.mp4"
cap = cv2.VideoCapture(video_path)

ret, frame = cap.read()

bbox = cv2.selectROI("Tracking", frame, False)
cv2.destroyWindow("Tracking")

tracker.init(frame, bbox)

while True:
    time.sleep(0.1)

    ret, frame = cap.read()
    if not ret:
        break

    success, bbox = tracker.update(frame)

    if success:
        (x, y, w, h) = [int(i) for i in bbox]

        cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 0), 2, 1)
    else:
        cv2.putText(frame, "Nesne Takibi Başarısız", (100,80), cv2.FONT_HERSHEY_SIMPLEX, 0.75, (0, 0, 255), 2)

    cv2.imshow("Tracking", frame)

    if cv2.waitKey(1) & 0xFF == ord("q"):
        break

cap.release()
cv2.destroyAllWindows()







