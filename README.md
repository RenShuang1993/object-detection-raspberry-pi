# object-detection-raspberry-pi

## ubuntu VNC
``` bash
sudo apt-get update
sudo apt-get upgrade
sudo apt-get install tightvncserver
vncserver -geometry 800×800 :1
```
open `Remote Desktop Viewer` and Connect with you IP
![](https://sqlandplsql.files.wordpress.com/2012/07/vinagre_connect.jpeg)

## Collecting Datasets via Raspberry Pi Camera
if use raspberrt pi camera:
Because my video is reddish, so i change the white balance
```python
from picamera import PiCamera
camera = PiCamera()
camera.awb_mode='off'
#change white balance 
camera.awb_gains=(1.0,1.2)
camera.resolution =(640 ,480)
```
if use usb camera:
```python
import cv2
video = cv2.VideoCapture(0)
```
## use opencv Saving Video Frames
```python
cap = cv2.VideoCapture("your video name")
```



