 number_of_soaps=int(input())
lst=list(map(int,input().split()))
n=int(input())
for i in range(n):
    M=int(input())
    c=0
    for j in lst:
        if(j<M):
            c+=1
    print(c)
        
