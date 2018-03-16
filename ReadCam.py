import numpy as np
import cv2
import time

cap = cv2.VideoCapture(1)


w = cap.get(cv2.CAP_PROP_FRAME_WIDTH);

h = cap.get(cv2.CAP_PROP_FRAME_HEIGHT);
i = 0
nam = "a"
# Define the codec and create VideoWriter object
fourcc = cv2.VideoWriter_fourcc(*'avc1')
out = cv2.VideoWriter(nam + str(i) + ".mp4", fourcc, 8.0, (int(w),int(h)))

while(True):
    _, frame = cap.read()
    # write the flipped frame
    cv2.imshow('frame', frame)
    out.write(frame)
    if cv2.waitKey(1) == 27:
        i = i+1
        out.release()
        out = cv2.VideoWriter(nam + str(i) + ".mp4", fourcc, 8.0, (int(w), int(h)))
        print("DONE")
    if i ==10:
        cap.release()
        out.release()
        cv2.destroyAllWindows()
        break

# Release everything if job is finished
