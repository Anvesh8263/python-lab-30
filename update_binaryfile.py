"""
creat a binary file with roll number, name and marks.
input roll number and update marks 
"""

# create a file with roll number, name and marks 

with open("binary_filemarks.txt", 'wb' ) as f:
    flag = 'Y'
    while flag != 'N' or flag != 'n':
        roll_n = int(input("Enter the roll number "))
        name = input("Enter the name ")
        marks = input("Enter the marks ")
        data = f"{roll_n}\t{name}\t{marks}\n"
        f.write(data.encode())
        flag = input("Do you want to enter another entry Y/N ")


# input roll number and update the marks 
with open("binary_filemarks.txt", 'rb+' ) as f:
    data = f.readlines()
    roll_n = input("Enter the roll number to update the marks ")
    marks = input("Marks: ")
    for c, line in enumerate(data):
        line = line.decode()
        if line.startswith(roll_n):
            tmp = line.split()
            tmp[-1] = marks
            tmp = '\t'.join(tmp).encode()
            break
    data[c] = tmp
    f.seek(0)
    f.writelines(data)
