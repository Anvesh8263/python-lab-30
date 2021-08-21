Python 3.9.6 (tags/v3.9.6:db3ff76, Jun 28 2021, 15:26:21) [MSC v.1929 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> def big(a, b):
    i = 0
    while a <= b:
        a, b, i = a*3, b*2, i+1
    print(i)


x, y = map(int, input().split())
big(x, y)