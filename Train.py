import cv2
import numpy as np
import time
from sklearn.ensemble import RandomForestClassifier
import test




names=['frunasverde', 'jumbomani', 'jet', 'chocorramo', 'frunasamarillo', 'frunasnaranjado', 'frunasrojo', 'jumboflowblanca', 'jumbomix']




#"TrainData/"+objnam+"0.mp4"
filter = np.ones((3,3))
cammera = cv2.VideoCapture("test0.mp4")
size = (700, 935)
center_mask = np.zeros((size))
#ser = serial.Serial('/dev/cu.usbmodem1411', baudrate=115200)
range_center = np.arange(np.int0(size[0]/2-50+100), np.int0(size[0]/2+50+100), 1, np.int0)
was_processed = False


def main():

    for name in names:
        for x in range(0, 5):
            camera = cv2.VideoCapture("Data/"+name+"/"+name+str(x)+".mp4")
            obj, mask = show_webcam(camera, cv2.createBackgroundSubtractorMOG2())
            camera.release()
            fts = get_features(obj, mask)
            np.save("Modelos/"+name+"/"+"features"+name+str(x), fts)
            was_processed = False

def get_frame_processed(cammera, substractor):

    ret_val, originalFrame = cammera.read()

    originalFrame = originalFrame[100:100+size[0], 460:460+size[1]]
    rmvBkgFrame = substractor.apply(originalFrame)
    _, rmvBkgFrame = cv2.threshold(rmvBkgFrame, 127, 255, cv2.THRESH_BINARY)
    blurredFrame = cv2.medianBlur(rmvBkgFrame, 5)
    blurredFrame2 = cv2.erode(blurredFrame, filter, iterations = 50)
    blurredFrame3 = cv2.dilate(blurredFrame2, filter, iterations = 90)
    cv2.imshow('Blurred Frame2', blurredFrame3)

    #cv2.rectangle(originalFrame, (0, np.int0(size[0]/2-50)), (size[1]-1, np.int0(size[0]/2+50)), (0,255,255), thickness=2, lineType=8, shift=0)


    return originalFrame, blurredFrame3


def f(x): return

def get_features(image, mask):


    features =[]

    # histB = cv2.calcHist([image], [0], mask, [3], [0, 256])
    # histG = cv2.calcHist([image], [0], mask, [3], [0, 256])
    # histR = cv2.calcHist([image], [0], mask, [3], [0, 256])

    hsv = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)
    hhist = cv2.calcHist([hsv], [0], mask, [3], [0, 180])

    shist = cv2.calcHist([hsv], [1],mask, [3], [0, 256])

    vhist = cv2.calcHist([hsv], [2], mask, [3], [0, 256])

    onehistr = np.vstack((hhist,shist,vhist))
    features.append(onehistr)
    features = np.squeeze(features)
    nonzero = np.count_nonzero(mask)
    features=np.append(features,nonzero)



    #np.save("features"+objnam, features)

    #print(features)


    return features



def show_webcam(cammera, substractor):

    threshold = 5
    i = 0
    initial_time = time.clock()
    idle_time = 10
    ser_flag = b'0'
    cv2.namedWindow("Reto 1", flags=cv2.WINDOW_NORMAL)
    cv2.moveWindow("Reto 1", 100, 0)
    cv2.createTrackbar("Velocidad banda", "Reto 1", 20, 100, f)

    center_mask = np.zeros((size))
    keep = True
    while keep:
        #ser.write(ser_flag)
        originalFrame, frame = get_frame_processed(cammera, substractor)
        showFrame = originalFrame.copy()

        cv2.imshow("Reto 1", originalFrame)

        _, contours, hierarchy = cv2.findContours(frame, cv2.RETR_LIST, cv2.CHAIN_APPROX_SIMPLE)
        average = np.average(frame)

        if average > threshold:

            #Find rectangle and draws it
            rect = cv2.minAreaRect(contours[0])
            box = cv2.boxPoints(rect)
            box = np.int0(box)
            cv2.drawContours(showFrame, [box], 0, (0, 0, 255), 2)

            #Finds Center of object and draws it
            point, _, _ = rect
            point = np.int0(point)
            cv2.circle(showFrame, (point[0], point[1]), 2, (0,0,255), thickness=-1, lineType=8, shift=0)
            cv2.circle(center_mask, (point[0], point[1]), 70, 255, thickness= -1, lineType=8, shift=0)
            Y, _ = np.nonzero(center_mask)

            #shows proccessed frame
            cv2.imshow("Reto 1", showFrame)

            #Controls band velocity


            #Finds when object is near center
            intersection = np.intersect1d(Y, range_center)
            if intersection.size > 80 and not was_processed:
                was_processed = True
                cv2.drawContours(rect_mask, [box], 0, (255,255,255), -1)
                rect_mask = cv2.erode(rect_mask,filter,iterations=20)
                object = cv2.bitwise_and(originalFrame, rect_mask)
                rect_mask=rect_mask[:,:,0]
                return object, rect_mask


            initial_time = time.clock()


        else:

            center_mask = np.zeros(size)
            rect_mask = np.zeros((700,935,3), dtype="uint8")
            ser_flag = b'0'
            was_processed = False
            if (time.clock() - initial_time) > idle_time:
                print("No object found for more than 3 seconds")

        if cv2.waitKey(1) == 27:
             break

    cv2.destroyAllWindows()




if __name__ == '__main__':
	main()
