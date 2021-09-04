a, b = map(int, input().split())
c = list(map(int, input().split()))
d = 0
for i in c:
    if i <= b:
        d+=1
    else:
        d+=2
print(d)
