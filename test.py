import cv2
import numpy as np
import time



# def show_webcam(mirror=False):
#     cam = cv2.VideoCapture(0)
#     while True:
#         ret_val, img = cam.read()
#         if mirror:
#             img = cv2.flip(img, 1)
#         cv2.imshow('my webcam', img)
#         if cv2.waitKey(1) == 27:
#             break  # esc to quit
#     cv2.destroyAllWindows()


filter = np.ones((3,3))
cammera = cv2.VideoCapture('out2.mp4')


# Define the codec and create VideoWriter object
fourcc = cv2.VideoWriter_fourcc(*'avc1')
out = cv2.VideoWriter("chocorramo.mp4", fourcc, 10.0, (800,935))



def get_frame_processed(substractor = cv2.createBackgroundSubtractorMOG2(),
                        cammera = cammera):

    ret_val, originalFrame = cammera.read()

    originalFrame = originalFrame[100:900, 460:1395]
    rmvBkgFrame = substractor.apply(originalFrame)
    _, rmvBkgFrame = cv2.threshold(rmvBkgFrame, 127, 255, cv2.THRESH_BINARY)
    blurredFrame = cv2.medianBlur(rmvBkgFrame, 5)
    blurredFrame2 = cv2.erode(blurredFrame, filter, iterations = 50)
    blurredFrame3 = cv2.dilate(blurredFrame2, filter, iterations = 70)
    cv2.imshow('Blurred Frame2', blurredFrame3)


    return originalFrame, blurredFrame3

def calibrate_band(calibrationDuration=10):

    print("Calibrating...")
    finalTime = time.clock() + calibrationDuration
    imageAverages = np.array([0])
    while time.clock() < finalTime:
        _, frame = get_frame_processed()
        imageAverages= np.append(imageAverages, np.average(frame))

    maximum = np.amax(imageAverages[5:])
    print("Calibration done")
    print(maximum)

    return maximum


def show_webcam():

    a = np.zeros((800, 935, 3))
    threshold = calibrate_band(5) + 5
    i = 0
    initial_time = time.clock()
    idle_time = 10

    while True:

        originalFrame, frame = get_frame_processed()
        cv2.imshow('contours', originalFrame)

        _, contours, hierarchy = cv2.findContours(frame, cv2.RETR_LIST, cv2.CHAIN_APPROX_SIMPLE)


        average = np.average(frame)

        if average > threshold:
            print("OBJETO")
            b, _ = get_frame_processed()
            a = b
            rect = cv2.minAreaRect(contours[0])
            box = cv2.boxPoints(rect)
            print(box)
            print("--------------")
            box = np.int0(box)
            print(box)
            print(cv2.arcLength(box, True))
            cv2.drawContours(originalFrame, [box], 0, (255, 0, 255), 2)
            #cv2.drawContours(originalFrame, contours[0], -1, (0, 255, 0), 3)
            cv2.imshow("contours", originalFrame)
            i= i+1
            np.save('a'+str(i), a)
            initial_time = time.clock()
        else:
            i = 0
            print("NO OBJETO")
            a = np.zeros((800, 935, 3))
            if (time.clock() - initial_time) > idle_time:
                print("No object found for more than 3 seconds")

        if cv2.waitKey(1) == 27:
             print(i)

    cv2.destroyAllWindows()


def get_properties(box, image):
    perimeter = cv2.arcLength(box, True)
    


def main():
	show_webcam()

if __name__ == '__main__':
	main()