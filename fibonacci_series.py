def fib(n):
    if n <= 1:
        return n
    else:

        return fib(n-1) + fib(n-2)

# print(fib(0))


num = int(input('enter the length of fibonacci series '))
for i in range(num):
    f = fib(i)
    print(f)
