import cv2
import os
images = 'Pictures/Pictures_11_'
if not os.path.exists(images):
    os.mkdir(images)

cap = cv2.VideoCapture("video_car_12.h264")
c =0
while(1):
    success,frame = cap.read()
    if success:
        cv2.imwrite(images+str(c)+'.jpg',frame)
        c=c+1
    else:
        break
cap.release()