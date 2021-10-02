n = int(input())
for i in range(n):
    a,b,d = map(int, input().split())
    l = [a,b]
    l.sort()
    if a == 1 or b == 1:
            if l[1]-l[0]<=d:
                print("YES")
            else:
                print("NO")
    else:
        for i in range(2,l[0]+1):
            if a%i==0 or b%i==0:
                if a%i!=0:
                    if a%i<=d:
                        print("YES")
                    else:
                        print("NO")            
                elif b%i!=0:
                    if b%i<=d:
                        print("YES")   
                    else:
                        print("NO")
