n = int(input())
s = input()
m = []

m = s.split(' ')

cnt = 0
for i in range(0, n):
    if int(m[i]) > 0:
        cnt += 1

print(cnt)