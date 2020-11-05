import os

#win下好用
def get_desk_p():
    t = os.path.join(os.path.expanduser('~'),"Desktop")
    print(t)

    return os.path.join(os.path.expanduser('~'),"Desktop")

print(get_desk_p())


