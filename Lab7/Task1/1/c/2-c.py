x = int(input())

s = 0
while 2 ** s < x+1:
    print(2 ** s)
    s += 1
