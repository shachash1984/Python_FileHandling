#!/usr/bin/python
import copy
"""
# open a file, read mode
f = open("python.txt", "r")
print(f.read())

# sets the file pointer back to the start of the file
# f.seek(0)

# reading a file incrementally
# great for big files

# correct way
for line in f:
    print(line, "1111")

# wrong way! - readlines() reads the entire file at once
for line in f.readlines():
    print(line, "1111")

# closing a file
f.close()
"""

# another way to handle file without explicitly calling close()
# (in order to prevent being thrown and leaving the file open)
# best practice
with open("File_Ex1.txt", 'r') as my_file:
    for line in my_file:
        line = line.replace('\n', '+')
        # print(line, end="")

# saving files to list
lines = list()
with open("File_Ex1.txt", 'r') as my_file:
    for line in my_file:
        lines.append(line)

lines_without_new_line = list()

for line in lines:
    line = line.replace('\n', "")
    lines_without_new_line.append(line)
print(lines_without_new_line)

reversed_list = copy.copy(lines_without_new_line)
reversed_list.reverse()

with open("python.txt", 'w') as my_file:
    for line in reversed_list:
        line_with_break = line+'\n'
        my_file.write(line_with_break)

with open("python.txt", 'r') as my_file:
    for line in my_file:
        print(line)

# TODO:
# create a file in python and write
# numbers 1 to 100 in every line of the file


with open("numbers.txt", 'w') as my_file:
    for i in range(0, 100):
        my_file.write(str(i+1)+'\n')

with open("numbers.txt", "a") as my_file:
    for i in range(200, 231):
        my_file.write(str(i) + '\n')

