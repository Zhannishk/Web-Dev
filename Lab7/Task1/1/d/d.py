n = int(input())
s = input()
m = []

m = s.split(' ')

cnt = 0
for i in range(1, n):
    if int(m[i]) > int(m[i-1]):
        cnt += 1

print(cnt)