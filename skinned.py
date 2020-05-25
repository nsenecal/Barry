import cv2
import os
import numpy

video = cv2.VideoCapture("myhead.mp4")
def getFrame(sec):
        video.set(cv2.CAP_PROP_POS_MSEC, sec*1000)
        hasFrames, image = video.read()
        if hasFrames:
            cv2.imwrite("image"+str(count)+".jpg", image)
        return hasFrames
sec = 0
frameRate = 1/30
count = 1
success = getFrame(sec)

length = int(video.get(cv2.CAP_PROP_FRAME_COUNT))
while success:
    count = count + 1
    sec = sec + frameRate
    sec = round(sec, 2)
    success = getFrame(sec)
    print(count)

count = 1
while os.path.isfile("image"+str(count)+".jpg"):
    image = cv2.imread("image"+str(count)+".jpg")
    height, width, channels = image.shape
    cropped = image[0:int(height),int((width/2)-1):int((width/2))]
    cv2.imwrite("image"+str(count)+".jpg", cropped)
    count = count + 1
    print(count)
    cv2.waitKey(0)

count = 1
while os.path.isfile("image"+str(count+1)+".jpg"):
    img1 = cv2.imread("image1.jpg")
    img2 = cv2.imread("image"+str(count+1)+".jpg")
    combined = numpy.concatenate((img1,img2),axis=1)
    cv2.imwrite("image1.jpg", combined)
    os.remove("image"+str(count+1)+".jpg")
    count = count + 1
    print(count)
cv2.imshow('image',img1)
cv2.waitKey(int(1/60))
