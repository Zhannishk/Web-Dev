x = int(input())

s = 2
while s < x+1:
    if x % s == 0:
        print(s)
        break
    s += 1
