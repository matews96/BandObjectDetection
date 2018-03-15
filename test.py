import cv2
import numpy as np
import time
#import serial



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
size = (700, 935)
center_mask = np.zeros((size))
#ser = serial.Serial('/dev/cu.usbmodem1411', baudrate=115200)
range_center = np.arange(np.int0(size[0]/2-50), np.int0(size[0]/2+50), 1, np.int0)
was_processed = False


def get_frame_processed(substractor = cv2.createBackgroundSubtractorMOG2(),
                        cammera = cammera):

    ret_val, originalFrame = cammera.read()

    originalFrame = originalFrame[100:100+size[0], 460:460+size[1]]
    rmvBkgFrame = substractor.apply(originalFrame)
    _, rmvBkgFrame = cv2.threshold(rmvBkgFrame, 127, 255, cv2.THRESH_BINARY)
    blurredFrame = cv2.medianBlur(rmvBkgFrame, 5)
    blurredFrame2 = cv2.erode(blurredFrame, filter, iterations = 50)
    blurredFrame3 = cv2.dilate(blurredFrame2, filter, iterations = 80)
    cv2.imshow('Blurred Frame2', blurredFrame3)
    cv2.rectangle(originalFrame, (0, np.int0(size[0]/2-50)), (size[1]-1, np.int0(size[0]/2+50)), (0,255,255), thickness=2, lineType=8, shift=0)


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

    threshold = calibrate_band(1) + 5
    i = 0
    initial_time = time.clock()
    idle_time = 10
    ser_flag = b'0'

    while True:
        #ser.write(ser_flag)
        originalFrame, frame = get_frame_processed()
        cv2.imshow('contours', originalFrame)

        _, contours, hierarchy = cv2.findContours(frame, cv2.RETR_LIST, cv2.CHAIN_APPROX_SIMPLE)


        average = np.average(frame)

        if average > threshold:
            rect = cv2.minAreaRect(contours[0])
            point, _, _ = rect
            point = np.int0(point)
            if not was_processed and point[1]>200:
                ser_flag = b'1'
            else:
                ser_flag = b'0'
            #print(point)
            box = cv2.boxPoints(rect)
            box = np.int0(box)
            cv2.drawContours(originalFrame, [box], 0, (255, 0, 255), 1)
            cv2.circle(center_mask, (point[0], point[1]), 70, 255, thickness= -1, lineType=8, shift=0)
            Y, _ = np.nonzero(center_mask)
            intersection = np.intersect1d(Y, range_center)
            print (intersection.size)
            cv2.imshow("ap", center_mask)

            if intersection.size == 100 and not was_processed:
                was_processed = True
                cv2.drawContours(rect_mask, [box], 0, (255,255,255), -1)
                print(np.shape(originalFrame))
                print(np.shape(rect_mask))
                object = cv2.bitwise_and(originalFrame, rect_mask)
                pos = np.nonzero(object)
                print(pos[0][1])
                print(pos[1][1])
                print(pos[2][1])
                cv2.imshow("jfhdfhdjf", object)
                cv2.imshow("mask", rect_mask)
                cv2.imshow('a', originalFrame)
                print("Bitch")


            #cv2.drawContours(originalFrame, contours[0], -1, (0, 255, 0), 3)
            cv2.circle(originalFrame, (point[0], point[1]), 50, (255,255,0), thickness=-1, lineType=8, shift=0)
            cv2.imshow("contours", originalFrame)
            i= i+1
            initial_time = time.clock()
        else:
            center_mask = np.zeros(size)
            rect_mask = np.zeros((700,935,3), dtype="uint8")
            cv2.imshow("ap", center_mask)
            ser_flag = b'0'
            was_processed = False
            if (time.clock() - initial_time) > idle_time:
                print("No object found for more than 3 seconds")

        if cv2.waitKey(1) == 27:
             print(i)

    cv2.destroyAllWindows()

def main():
	show_webcam()

if __name__ == '__main__':
	main()