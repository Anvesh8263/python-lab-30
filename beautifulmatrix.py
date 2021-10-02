matrix = []
for i in range(5):
    matrix.append(input().split())
h = 1
for i in matrix:
    for j in range(5):
        if i[j]=='1':
            x = h
            b=j+1
    h+=1
k = abs(x-3)+abs(b-3)
print(k)
