# read_temp_file.py
# Ethan Bryant HW5
# ECS32A Dr. Kristian Stevens
# Takes a csv file and manipulates data

inp = input("Temperature anomaly filename:")
infile = open(inp, "r") # opens file
infile.readline() # skips Year,Value

for line in infile:
    
    line = line.strip("\n").split(",") # creates a list of the two strings in line
    year = line[0]
    temp = float(line[1])
    
    print(f"{year} {temp}") # prints output