Python 3.9.6 (tags/v3.9.6:db3ff76, Jun 28 2021, 15:26:21) [MSC v.1929 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> n =input()

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