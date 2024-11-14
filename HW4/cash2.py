# cash2.py
# Ethan Bryant HW4
# ECS32A Dr. Kristian Stevens
# sums numbers with features!

print("Automated cash register")

total = 0
i=0
# input filename
file_name = input("Enter file of prices:")
# file opened for reading
infile = open(file_name, "r")

for line in infile:
# strip whitespace from ends
    line = line.strip()
    line = line[1:]
    num = line[0] + line[2:]
    if num.isnumeric():
        total += float(line)
        i +=1
        
print("File contained", i, "items totaling $" + format(total, ".2f"))
