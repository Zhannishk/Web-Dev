def xor(a, b):
    print(int((not(a) and b) or (a and not(b))))


x, y = map(int, input().split())
xor(x, y)