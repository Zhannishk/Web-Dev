a, b, c, d = map(int, input().split())

def minimum(a, b, c, d):
    l = [a, b, c, d]
    l.sort()
    print(l[0])

minimum(a, b, c, d)
