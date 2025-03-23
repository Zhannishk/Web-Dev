n = int(input())
s = input()
m = []

m = s.split(' ')

for i in range(1, n):
    if int(m[i]) * int(m[i-1]) > 0:
        print("YES")
        break

else:
    print("NO")