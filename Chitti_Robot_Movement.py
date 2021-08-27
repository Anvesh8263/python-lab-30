 l=list(input())

a=0

b=0

for i in range(len(l)):

    if(l[i]=='L'):

        a+=1

    elif(l[i]=='R'):

        a-=1

    elif(l[i]=='U'):

        b+=1

    elif(l[i]=='D'):

        b-=1

if((a==0)and(b==0)):

    print("true")

else:

    print("false")
