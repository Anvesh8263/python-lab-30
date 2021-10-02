a =int(input())
for i in range(a):
    c = 0
    for i in range(1,int(input())+1):
        l = str(i)
        n = len(l)
        h = n-1
        for i in range(n):
            if l[i]!=l[h]:
                break
            else:
                h-=1
        else:
            c+=1
    print(c)
