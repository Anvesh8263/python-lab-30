a = int(input())
b = input()
x,y = b.count('A'),b.count('D')
if x > y:
    print("Anton")
elif x < y:
    print("Danik")
else:
    print("Friendship")
