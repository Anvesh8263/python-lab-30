 l=list(map(int,input().split()))

sum_=0

for i in l:

    sum_ = sum_ + ~i

if sum_%10==0:

    print('YES')

else:

    print('NO')
