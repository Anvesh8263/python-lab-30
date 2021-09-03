num=int(input("enter the number"))

cakebar=input().split()

cakebar=list(map(int,cakebar))

c1,c1=num,0

for i in range(num):
    
    if cakebar[i]==1:
       
         c1=i
       
          break

p=range(num)

for i in c[num-1::-1]:
    
     if cakebar[i]==1:
       
          c2=i
       
          break

d=0

for i in range(c1,c2-1):
     
     if cakebar[i]==1:
         
         if cakebar[i+1] !=1:
            
                  d+=1
    
        else :
         
                (d+=1)

    print(d+1)
