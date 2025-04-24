import cv2
import time
import mediapipe as mp
import handtrackingmodule as htm
import math
import osascript
import numpy as np



cap= cv2.VideoCapture(1)
pTime=0
detector=htm.handDetetor(detectionCon=0.7)

vol=0
volBar=400

while True:
    success,img=cap.read()
    img=detector.findHands(img)
    lmlist=detector.findPosition(img,draw=False)
    if len(lmlist)!=0:
        # print(lmlist[4],lmlist[8])
        x1,y1=lmlist[4][1],lmlist[4][2]
        x2,y2=lmlist[8][1],lmlist[8][2]
        cx,cy=(x1+x2)//2,(y1+y2)//2

        cv2.circle(img,(x1,y1),15,(120,120,120),cv2.FILLED)
        cv2.circle(img,(x2,y2),15,(120,120,120),cv2.FILLED)
        cv2.circle(img,(cx,cy),15,(120,120,120),cv2.FILLED)
        cv2.line(img,(x1,y1),(x2,y2),(120,120,120),2)
        length=math.hypot(x2-x1,y2-y1)

        if length<50:
            cv2.circle(img,(cx,cy),15,(0,255,0),cv2.FILLED)
        
        vol = int(np.interp(length, [50, 300], [0, 100]))
        volBar=np.interp(length,[50,300],[400,150])
        volPer=np.interp(length,[50,300],[0,100])
        osascript.osascript(f"set volume output volume {vol}")


        cv2.rectangle(img,(50,150),(85,400),(120,120,120),2)
        cv2.rectangle(img,(50,int(volBar)),(85,400),(120,120,120),cv2.FILLED)
        cv2.putText(img, f'{int(vol)} %', (40, 450),
            cv2.FONT_HERSHEY_COMPLEX, 1, (255, 255, 255), 2)

    cTime=time.time()
    fps=1/(cTime-pTime)
    pTime=cTime

    cv2.putText(img,f'Fps:{int(fps)}',
                (20,50),cv2.FONT_HERSHEY_COMPLEX,2,(127,127,127),2)
    
    cv2.imshow("Image",img)
    cv2.waitKey(1)
