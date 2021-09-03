 ln = int(input())
lst = input().split()
lst = ''.join(lst)
n = int(input())

lstt = []

for i in range(1,ln+1):
    lstt.append(i)

g = list(combinations(lstt,n))

count = 0
c = 0
lst_index = []

for a,pl in enumerate(lst,1):
    if pl == 'a':
        lst_index.append(a)



for kk in g:
    c += 1
    for i in lst_index:
        print(i,'in',kk)
        if i in kk:
            count += 1
            break # need to check 1 for satisfy

print(count)

h = count/c
print(h)
