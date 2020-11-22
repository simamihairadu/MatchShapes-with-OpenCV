import cv2
import numpy as np
import ShapeSetup

frameWidth = 640
frameHeight = 480
cap = cv2.VideoCapture(0)
cap.set(3, frameWidth)
cap.set(4, frameHeight)

def empty(a):
    pass

cv2.namedWindow("Parameters")
cv2.resizeWindow("Parameters",640,240)
cv2.createTrackbar("Threshold1","Parameters",64,255,empty)
cv2.createTrackbar("Threshold2","Parameters",164,255,empty)


def getShapeContour(imgContour):
    shapeArray = ShapeSetup.SetUp()
    for s in shapeArray:
        shape = cv2.imread(s.filePath, 0)
        ret, thresh = cv2.threshold(shape, 127, 255, 0)
        inverse = cv2.bitwise_not(thresh)
        contours, hierarchy = cv2.findContours(inverse, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)
        for c in contours:
            result = cv2.matchShapes(c, imgContour, 1, 0.0)
            s.value = result
    return shapeArray

def getContours(img, imgContour):

    contours, hierarchy = cv2.findContours(img, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)
    for cnt in contours:
        area = cv2.contourArea(cnt)
        if area > 2000:
            resultArray = getShapeContour(cnt)
            resultArray.sort(key=lambda x: x.value)
            peri = cv2.arcLength(cnt, True)
            approx = cv2.approxPolyDP(cnt, 0.02 * peri,True)
            x , y , w , h = cv2.boundingRect(approx)
            cv2.rectangle(imgContour,(x,y), (x + w , y + h), (0,255,0),3)

            cv2.putText(imgContour,resultArray[0].name,(x+w+20,y+45),cv2.FONT_HERSHEY_COMPLEX,0.7,(0,255,255),2)

while True:
    success, img = cap.read()
    imgContour = img.copy()
    imgBlur = cv2.GaussianBlur(img, (7, 7), 1)
    imgGray = cv2.cvtColor(imgBlur,cv2.COLOR_BGR2GRAY)


    threshold1 = cv2.getTrackbarPos("Threshold1","Parameters")
    threshold2 = cv2.getTrackbarPos("Threshold2","Parameters")
    imgCanny = cv2.Canny(imgGray,threshold1,threshold2)
    kernel = np.ones((5,5))
    imgDilate = cv2.dilate(imgCanny, kernel)

    getContours(imgDilate,imgContour)

    cv2.imshow("Source", imgContour)
    cv2.imshow("Canny", imgDilate)
    exit = cv2.waitKey(1)
    if exit == 27:
        break;

