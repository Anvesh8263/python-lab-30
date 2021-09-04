n = int(input())
b = 0
for i in range(n):
    v = list(input().split())
    if v.count('1')>=2:
        b+=1
print(b)
