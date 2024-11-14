# cat.py
# Ethan Bryant HW4
# ECS32A Dr. Kristian Stevens
# Was demonstrated in lecture, prints lines

# input filename
file_name = input("Enter a file name to open:")
# file opened for reading
infile = open(file_name, "r")

for line in infile:
# strip whitespace from ends
    line = line.strip()
    print(line)
