import cv2

def main():
    capture = cv2.VideoCapture('c.mp4')

    while (capture.isOpened()):
        ret, frame = capture.read()
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

        cv2.imshow('frame', frame)

        #表示暂停时间 值越大，视频播放速度越慢
        if cv2.waitKey(30) == ord('q'):
            break


if __name__ == '__main__':
    main()