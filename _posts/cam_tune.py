#!/usr/bin/env python
# -*- coding: utf-8 -*-
####################################################################
# 프로그램명 : hough_drive_c1.py
# 작 성 자 : (주)자이트론
# 생 성 일 : 2020년 07월 23일
# 본 프로그램은 상업 라이센스에 의해 제공되므로 무단 배포 및 상업적 이용을 금합니다.
####################################################################


import os
import cv2
import sys
import rospy
import signal
import numpy as np

from sensor_msgs.msg import Image
from cv_bridge import CvBridge, CvBridgeError

def signal_handler(sig, frame):
    import time
    time.sleep(3)
    os.system('killall -9 python rosout')
    sys.exit(0)

signal.signal(signal.SIGINT, signal_handler)

bridge = CvBridge()
cv_image = np.empty(shape=[0])
ack_publisher = None

def img_callback(data):
    global cv_image
    try:
      cv_image = bridge.imgmsg_to_cv2(data, "bgr8")
    except CvBridgeError as e:
      print(e)

rospy.sleep(3)
bridge = CvBridge()
image_sub = rospy.Subscriber("/usb_cam/image_raw/",Image,img_callback)
rospy.init_node('cam_tune', anonymous=True)
    
garo = 7
sero = 15
color = (255, 255, 255)

while cv_image.size == (320*240*3):
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

    constant = cv_image.copy()

    for g in range(1, garo+1):
        x = g*int(320/(garo+1))
        constant = cv2.line(constant, (x, 0), (x, 239), color, 1)

    for s in range(1, sero+1):
        y = s*int(240/(sero+1))
        constant = cv2.line(constant, (0, y), (319, y), color, 1)

    cv2.imshow("cam_tune", constant)

cv2.destroyAllWindows()
















