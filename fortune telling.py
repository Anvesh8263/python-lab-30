import itertools 
a = int(input())
n = list(map(int, input().split())) 
com = []
for i in range(a+1):
    c = itertools.combinations(n,i)
    com.append(c)
k = []
for i in com:
    for j in i:
        if sum(j)%2!=0:
            k.append(sum(j))
if len(k)==0:
    print(0)
else:
    print(max(k))
