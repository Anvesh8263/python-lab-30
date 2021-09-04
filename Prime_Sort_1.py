a=input()

b=[]

for i in a :

    if i=='2' or i=='3' or i=='5' or i=='7' :

        b.append(i)

        a=a.replace(str(i),"",1)

b.sort()

c=''

for i in b :

    c=c+str(i); 

print('"'+c+a[1:-1]+'"')
