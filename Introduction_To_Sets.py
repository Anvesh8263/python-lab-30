def average(array):
    ar = set(arr)
    result = 0
    c = 0
    for i in ar:
        result += i
        c += 1
    d = result / c
    return d


if _name_ == '_main_':
    n = int(input())
    arr = list(map(int, input().split()))
    result = average(arr)
    print(result)


