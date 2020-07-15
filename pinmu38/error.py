"""import os, concurrent.futures

def merge(path, name):
    with open(os.path.join(path, "ts.m3u8"), "r+") as f:
        ts_list = f.readlines()
        print(ts_list)
    book = open(os.path.join(path, "{}.mp4".format(name)), "ab+")
    for t in ts_list:
        try:
            with open(t, "rb+") as f:
                b = f.read()
            book.write(b)
            os.remove(t)
        except:
            with open(os.path.join(path, "未写入.txt"), "a+") as f:
                f.write(t)
                f.write("\n")
    book.close()

def main():
    path = r"N:\codes\m3"

    file_dirlist = os.listdir(path) #读目录


    path_list = [os.path.join(path, i) for i in file_dirlist] #路径
    print(path_list)
    merge()

    #path_name_list = list(zip(file_dirlist, path_list))

    #with concurrent.futures.ThreadPoolExecutor(max_workers=10) as process:
    #   fun1 = [process.submit(merge, p[1], p[0]) for p in path_name_list]

if __name__ == "__main__":
    main()
    print("完成")"""
