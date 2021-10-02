n = int(input())
for i in range(n):
    a = int(input())
    b = input()
    if b.count("1")/a==0.5:
        print("YES")
    else:
        m = 1
        for j in range(a):
            if b[j] == "1":
                if m/j+1==0.5:
                    print("YES")
                    break
                else:
                    m+=1
        else:
            print("NO")
