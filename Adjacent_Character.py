 n =input()

output = ''

i = 0

if len(n)% 2==0:

    while i < len(n):

        if i + 1 < len(n):

            output = output + n[i + 1]

            output = output + n[i]

        i = i + 2

    print(output)

else:

    print("Odd length.")
