t = int(input())
while t!=0:
    c = 0
    a = input(); b = input()
    for i in range(len(a)):
        for j in range(len(b)):
            if a[i]==b[j] or ord(a[i])-32 == ord(b[j]) or ord(a[i])+32 == ord(b[j]):
                c+=1
    if c == len(b):
        print("YES")
    else:
        print("NO")           
    t-=1
