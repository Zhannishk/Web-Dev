n = int(input())
s = input()
m = []

m = s.split(' ')

res = ''
for i in range(0, n):
    if int(m[i]) % 2 == 0:
        res += m[i] + ' '

print(res)