n=int(input("Enter the length: "))
i=0
while n>0:
    if n>=5:
        n=n-5
        i=i+1
    if n>=4:
        n=n-4
        i=i+1
    if n>=3:
        n=n-3
        i=i+1
    if n>=2:
        n=n-2
        i=i+1
    if n>=1:
        n=n-1
        i=i+1
else:
    print(i)    
