a = input()
c=0
c1=0
for i in a:
    if i.isupper():
        c+=1
    elif i.islower():
        c1+=1
if c>c1:
    print(a.upper())
elif c1>=c:
    print(a.lower())
