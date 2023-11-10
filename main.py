from random import randint

a = 0
b = 1000
c = randint(a, b)
e = 1

# print(c)

while 1 == 1:
    d = int(input("введите число "))
    if d == c:
        print("ви угадали")
        print(f"ви угадали за {e} ходов")
        exit()
    if d > c:
        print("меньше")
    if d < c:
        print("больше")

    e = e + 1
