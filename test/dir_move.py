import os, shutil
import platform
import time

def dir(): #linux
    filename = "./Finance"
    isExists = os.path.exists(filename)
    if not isExists:
        os.mkdir(filename)

    path = "./Finance/"
    filename = "./New_Finance.xlsx"
    #filename = "./Finance/News_Finance.xlsx"
    if not path:
        os.mkdir(path)
    filetime = time.strftime("%Y_%m_%d_%H_%M", time.localtime())  # year-month-day-hour-minute
    path2 = path + "闻讯__" + filetime + ".xlsx"
    shutil.move(filename, path2)


def win_filemove():
    print(123)


def plat():
    sys = platform.system()
    if sys == "Windows":
        win_filemove()
    elif sys == "Linux":
        dir()


if __name__ == "__main__":
    plat()
