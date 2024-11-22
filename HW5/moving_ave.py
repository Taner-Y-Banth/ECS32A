# moving_ave.py
# Ethan Bryant HW5
# ECS32A Dr. Kristian Stevens
# Calculates a moving average

inp = input("Temperature anomaly filename:")
infile = open(inp, "r") # opens file
infile.readline() # skips Year,Value
list = []

k = int(input("Enter window size:"))

for line in infile:
    
    line = line.strip("\n").split(",") # creates a list of the two strings in line
    year = line[0]
    temp = float(line[1])
    list.append(temp)

index = k

for index in range(k, len(list) - k): # loops to print moving avg
    year = 1880 + index
    avg = sum(list[index-k:index+k+1]) / (2*k+1) # averages from a sum of range list[a:b]
    print(f"{year},{avg:.4f}") # prints output and formats avg to 4 decimal places
