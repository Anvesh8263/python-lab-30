 a = int(input())

for i in range(a):
    n1, n2 = input().split()
    try:
        print(int(n1)//int(n2))
    except Exception as e:
        print('Error Code:', e)
