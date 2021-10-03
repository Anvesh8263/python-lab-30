import itertools 
a = int(input())
n = list(map(int, input().split()))
com = []
for i in range(a+1):
    c = itertools.combinations(n,i)
    for x in c:
    	if sum(x)%2!=0:
    		com.append(sum(x))

if len(com)==0:
    print(0)
else:
    print(max(com))
