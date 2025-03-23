n = int(input())
m = input().split()

for i in range(n//2):
    m[i], m[n-i-1] = m[n-i-1], m[i]
    if i == (n-i):
        break

print(*m)