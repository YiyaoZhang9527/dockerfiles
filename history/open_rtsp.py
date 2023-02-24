#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Oct  5 03:11:31 2020

@author: prabhakar
"""

import cv2

cv2.namedWindow("RTSP View", cv2.WINDOW_NORMAL)
ip_address = "192.168.16.165"
cap = cv2.VideoCapture(f"rtsp://{ip_address}:8554/video_stream")
while True:
    ret, frame = cap.read()
    if ret:
        cv2.imshow("RTSP View", frame)
        cv2.waitKey(1)
    else:
        print("unable to open camera")
        break
cap.release()
cv2.destroyAllWindows()
