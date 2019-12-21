from picamera.array import PiRGBArray
from picamera import PiCamera
import cv2
import time
import io

        
camera = PiCamera()
camera.awb_mode='off'
camera.awb_gains=(1.0,1.2)
camera.resolution =(640 ,480)
camera.iso = 400
camera.framerate = 10
rawCapture = PiRGBArray(camera,size=(640,480))
#file
fourcc = cv2.VideoWriter_fourcc(*'XVID')
out = cv2.VideoWriter('./video_car_12.h264',fourcc,10,(640 ,480))
#warm up
time.sleep(1)
for frame in camera.capture_continuous(rawCapture,format="bgr",use_video_port=True):
    image = frame.array
    cv2.imshow("Frame",image)
    key=cv2.waitKey(1) & 0xFF
    out.write(image)
    rawCapture.truncate(0)
    if key == ord("q"):
        break