import platform

def get_sysinfo():
    sys = platform.system()
    if sys == "Windows":
        print("OS is Windows!!!")
    elif sys == "Linux":
        print("OS is Linux!!!")

print(get_sysinfo())
