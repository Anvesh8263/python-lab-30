 n=eval(input())
m=eval(input())
c=0
for i in range(len(n)):
    for j in range(len(m)):
        if str(sorted(n[i]))==str(sorted(m[j])):
            c+=1
print(c)

