n = int(input())
for i in range(n):
    a,b = map(int, input().split())
    if 1<=a<=100 and 1<=b<=10:
        print(a//b)
