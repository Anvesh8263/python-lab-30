n = int(input())
a = list(map(int, input().split()))
z = 1
while z>0:
    l = 0
    for i in range(n-1):
        if a[i]>a[i+1]:
            k = a[i]-a[i+1]
            a[i+1]+=k
            a[i]-=k
            l = 1
    if l==0:
        break
print(*a)
