import math


def main():
    print('q_math(2, 3, 1) = ', q_math(2, 3, 1))
    print('q_math(1, 3, -4) = ', q_math(1, 3, -4))


def q_math(a, b, c):
    in_a = float(b **2 - 4 * a * c)
    if in_a < 0:
        printf('no Result')
    x1 = -b + (math.sqrt(in_a)) / (2 * a)
    x2 = -b - (math.sqrt(in_a)) / (2 * a)
    if in_a >= 0:
        print('x1: ', x1, 'x2: ', x2)
        return x1, x2



if __name__ == "__main__":
    main()
