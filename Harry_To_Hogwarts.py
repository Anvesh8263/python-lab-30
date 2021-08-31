def m(a):

    b=[int(a[0]),int(a[1]),int(a[2]),int(a[3])]

    b.sort()

    c=str(b[0])+str(b[1])+str(b[2])+str(b[3])

    return c

a=input()

count=0

while(a != '6174'):

    m1=m(a)

    m2=m1[::-1]

    a=str(int(m2)-int(m1))

    count=count+1

print(count)
