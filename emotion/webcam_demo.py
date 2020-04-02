#!/usr/bin/env python3
import cv2
import os
import keras
import face_recognition as fr
import numpy as np

vid=cv2.VideoCapture(0)
keys=["angry","disgust","scared","happy","sad","surprised","neutral"]

model=keras.models.load_model("emotion_cnn.h5")

def do_emotion(frame):
    global emotion,model
    rgb_frm=frame[:,:,::-1]
    faces=fr.face_locations(rgb_frm)
    if len(faces)<1:
        return frame
    face=faces[0]
    top,right,bottom,left=face
    frame=cv2.rectangle(frame,(left,top),(right,bottom),(0,0xFF,0),2)
    face_roi=frame[top:bottom,left:right]
    face_roi=cv2.cvtColor(face_roi,cv2.COLOR_BGR2GRAY)
    face_roi=cv2.resize(face_roi,(48,48))
    [emotion,]=model.predict(np.reshape(face_roi,(1,48,48,1)))
    os.system("clear")
    for i,a in enumerate(emotion):
        print("%s: %f%%" % (keys[i],a*100))
    return frame

while vid.isOpened():
    status,frame=vid.read()
    if status==False:
        break
    frame=cv2.flip(frame,1)
    frame=cv2.resize(frame,(0,0),fx=1/4,fy=1/4)
    frame=do_emotion(frame)
    cv2.imshow("Your emotion",frame)
    if cv2.waitKey(1) & 0xFF==ord('q'):
        break
