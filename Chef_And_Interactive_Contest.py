Python 3.9.6 (tags/v3.9.6:db3ff76, Jun 28 2021, 15:26:21) [MSC v.1929 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> n, m=map(int, input().split())
for i in range(n):
    n=int(input())
    if n>=m:
        print('Good boi')
    else:
        print('Bad boi')