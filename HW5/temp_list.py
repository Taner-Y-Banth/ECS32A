# temp_list.py
# Ethan Bryant HW5
# ECS32A Dr. Kristian Stevens
# Makes a list of temps

inp = input("Temperature anomaly filename:")
infile = open(inp, "r") # opens file
infile.readline() # skips Year,Value
list = [] # init list

for line in infile:
    
    line = line.strip("\n").split(",") # creates a list of the two strings in line
    year = line[0]
    temp = float(line[1])
    list.append(temp) # adds temp to a list
    
print(list)