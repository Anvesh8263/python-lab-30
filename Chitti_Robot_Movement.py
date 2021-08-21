Python 3.9.6 (tags/v3.9.6:db3ff76, Jun 28 2021, 15:26:21) [MSC v.1929 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> l=list(input())

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