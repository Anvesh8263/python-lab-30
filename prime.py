c=0

x=int(input("Enter the number"))

for i in range (1,x+1):
    
    if(x%i==0):
      
      c=c+1

if(c==2):
    
    print("Prime Number")

else:
    
    print("Not a Prime Number")