import threading
import time

mutex = threading.Lock()

def t1():
    mutex.acquire()
    print('t1')
    time.sleep(5)
    mutex.release()

def t2():
    print('t2')

if __name__ == '__main__':
    thread_list = []
    thread_list2 = []
    for i in range(3):
        t = threading.Thread(target=t1)
        t2 = threading.Thread(target=t2)
        thread_list.append(t)
        thread_list2.append(t2)


    for t in thread_list:
        t.start()

    for t in thread_list:
        t.join()