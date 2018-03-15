import numpy as np
import cv2

cap = cv2.VideoCapture(0)


w = cap.get(cv2.CAP_PROP_FRAME_WIDTH);

h = cap.get(cv2.CAP_PROP_FRAME_HEIGHT);

i = 0

# Define the codec and create VideoWriter object
fourcc = cv2.VideoWriter_fourcc(*'avc1')
out = cv2.VideoWriter("jbnjhbg.mp4", fourcc, 10.0, (int(w),int(h)))

while(cap.isOpened()):
    ret, frame = cap.read()
    if ret==True:
        frame = cv2.flip(frame,0)

        # write the flipped frame
        out.write(frame)

        cv2.imshow('frame',frame)
        if cv2.waitKey(1) == 27:
            i = i+1
            out = cv2.VideoWriter("aadad" + str(i) + ".mp4", fourcc, 10.0, (int(w), int(h)))
    else:
        break

# Release everything if job is finished
cap.release()
out.release()
cv2.destroyAllWindows()