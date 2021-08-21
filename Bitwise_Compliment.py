Python 3.9.6 (tags/v3.9.6:db3ff76, Jun 28 2021, 15:26:21) [MSC v.1929 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> l=list(map(int,input().split()))

sum_=0

for i in l:

    sum_ = sum_ + ~i

if sum_%10==0:

    print('YES')

else:

    print('NO')