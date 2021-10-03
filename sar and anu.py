n = int(input())
for i in range(n):
    a,b,c = map(int, input().split())
    v = 0
    z = 0
    for i in range(a):
        x = input()
        if x[0] in 'EQUINOX':
            v+=b 
        else:
            z+=c 
    if z>v:
        print("ANURADHA")
    elif v>z:
        print("SARTHAK")
    else:
        print("DRAW")
