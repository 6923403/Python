import os

def dir(): #linux
    filename = "./Finance"
    isExists = os.path.exists(filename)
    if not isExists:
        os.mkdir(filename)


if __name__ == "__main__":
    dir()
