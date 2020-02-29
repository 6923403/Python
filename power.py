def power(x):
    return x * x
 
def power2(x, n):
    s = 1
    while n > 0:
        n = n -1
        s = s * x
    return s

def main():
    x = input()
    x = int(x)
    print(power(x))

    print('\n power2: \n',power2(x, 3))

if __name__ == "__main__":
    main()
