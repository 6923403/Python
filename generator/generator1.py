#L = [x * x for x in range(10)]

'''
g = (x * x for x in range(10))
<generator object <genexpr> at 0x000001D8054AD548>
next g
'''
g = (x * x for x in range(10))
#for n in g:
   # print(n)

def fib(max):
    n, a, b = 0, 0, 1
    while n < max:
        #print(b)
        yield b
        a, b = b, a + b
        n = n + 1
    return 'done'



def main():
    fib(7)


if __name__ == '__main__':
    main()
