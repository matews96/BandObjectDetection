import numpy as np
import cv2
import time

cap = cv2.VideoCapture(1)


w = cap.get(cv2.CAP_PROP_FRAME_WIDTH);

h = cap.get(cv2.CAP_PROP_FRAME_HEIGHT);

i = 0

# Define the codec and create VideoWriter object
fourcc = cv2.VideoWriter_fourcc(*'avc1')
out = cv2.VideoWriter("jbnjhbg.mp4", fourcc, 10.0, (int(w),int(h)))
cv2.namedWindow('c', flags = cv2.WINDOW_GUI_NORMAL)

while(cap.isOpened()):
    initial_time = time.clock()
    ret, frame = cap.read()
    if ret==True:

        # write the flipped frame
        out.write(frame)

        #cv2.imshow('frame',frame)
        if cv2.waitKey(1) == 27:
            i = i+1
            out = cv2.VideoWriter("Jet/jet" + str(i) + ".mp4", fourcc, 10.0, (int(w), int(h)))
    else:
        break
# Release everything if job is finished
cap.release()
out.release()
cv2.destroyAllWindows()