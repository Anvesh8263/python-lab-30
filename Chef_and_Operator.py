Python 3.9.6 (tags/v3.9.6:db3ff76, Jun 28 2021, 15:26:21) [MSC v.1929 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> for i in range(int(input())):
    n=input().split()
    if int(n[0])<int(n[1]):
        print('<')
    elif int(n[0])>int(n[1]):
        print('>')
    else:
        print('=')