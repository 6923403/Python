import cv2

def main():
    capture = cv2.VideoCapture(0)
    fourcc = cv2.VideoWriter_fourcc(*"XVID")
    outfile = cv2.VideoWriter("autoVideo.avi", fourcc, 25., (640, 480))
    n = 300
    while (True):
        n = n - 1
        if n > 0:
            capture.isOpened()
        else:
            break
        ret, frame = capture.read()

        if ret:
            outfile.write(frame)  # 写入文件
            cv2.imshow('frame', frame)
            if cv2.waitKey(1) == ord('q'):
                break
        else:
            break

    capture.release()

if __name__ == '__main__':
    main()