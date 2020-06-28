# -*- coding: utf-8 -*-

# 导入cv模块
import cv2

cap = cv2.VideoCapture(0)

# 分类器下载地址 https://github.com/opencv/opencv/tree/master/data/haarcascades
# 使用OpenCV输入人脸识别分类器的位置
classfier = cv2.CascadeClassifier("N:\\codes\\Python\\opencv\\xm\\haarcascade_frontalface_default.xml")

#人嘴巴和鼻子识别
# classfier = cv2.CascadeClassifier("G://pythonCode//ContestDemo//xml//haarcascade_frontalcatface.xml")

#笑脸识别
# classfier = cv2.CascadeClassifier("G://pythonCode//ContestDemo//xml//haarcascade_smile.xml")

while True:
    # capture frame-by-frame
    ret, frame = cap.read()

    # our operation on the frame come here
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # 人脸检测，1.2和2分别为图片缩放比例和需要检测的有效点数
    faceRects = classfier.detectMultiScale(gray, scaleFactor=1.2, minNeighbors=3, minSize=(32, 32))
    if len(faceRects) > 0:  # 大于0则检测到人脸
        for faceRect in faceRects:  # 单独框出每一张人脸
            x, y, w, h = faceRect
            faceimg = cv2.rectangle(frame, (x - 10, y - 10), (x + w + 10, y + h + 10), (0, 255, 0), 2)


    # 展示结果
    cv2.imshow('frame', frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):  # 按q键退出
        break
# when everything done , release the capture
cap.release()
cv2.destroyAllWindows()
