 a=int(input())
b=input()
c=int(input())
for i in range(c):
    d=int(input())
    print(b.count(b[d-1],0,d-1))
