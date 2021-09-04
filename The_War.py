 i,j = map(int,input().split(" x "))

l = [(a,b) for a in range(i) for b in range(j) if (a+b)%2 != 0]

print(len(l))
