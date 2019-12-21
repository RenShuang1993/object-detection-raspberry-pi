# Object-detection-raspberry-pi
## install tensorflow and Object detection on raspberry pi 
### install tensorflow 
  TensorFlow：1.9<br>
  Python：3.5.3<br>
  Hardware: Raspberry 3B<br>
  install ibatlas-base-dev 
  ```bash
  sudo apt-get install libatlas-base-dev
  Do you want to continue? [Y/n] input：Y
  ```
  install tensorflow
  ```bash
  sudo pip3 install  tensorflow
  ```
  install other Dependent tools :numpy，tensorboard，markdown .....<br>
  in my case is tensorflow 1.9 so numpy version is 1.13.0,if numpy 1.16 or higher is not work
### install Object detetion model
see https://github.com/tensorflow/models/blob/master/research/object_detection/g3doc/installation.md

### install opencv
see https://www.learnopencv.com/install-opencv-4-on-raspberry-pi/

## Ubuntu VNC
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
## Use opencv Saving Video Frames
```python
cap = cv2.VideoCapture("your video name")
```
## Lable the ground truth
see https://github.com/tzutalin/labelImg
save as xml file

## XML file to CSV 

## CSV to TFCODE

## Create a .pbtxt file/label map file
Create a `train.pbtxt` file in object_detection/data
```python
item {
 id: 1
 name: 'car'
}
```
## Change `.config`file 
Download model https://github.com/tensorflow/models/blob/master/research/object_detection/g3doc/detection_model_zoo.md <br>
in my case ssd_mobilenet_v1_coco.config
Items to modify in the `.config`:
  *model.ssd.num_classes
  *train_config.fine_tune_checkpoint
  *train_input_reader.label_map_path
  *train_input_reader.tf_record_input_reader
  *eval_input_reader.label_map_path
  *eval_input_reader.tf_record_input_reader
## start to Train 
```bash

cd research/object_detection

python3 model_main.py \
--pipeline_config_path=data/ssd_mobilenet_v1_coco.config \
--model_dir=data/training \
--num_train_steps=60000 \
--num_eval_steps=20 \
--alsologtostderr
```


