# moving_ave.py
# Ethan Bryant HW5
# ECS32A Dr. Kristian Stevens
# 

inp = input("Temperature anomaly filename:")
infile = open(inp, "r") # opens file to read
infile.readline() # skips Year,Value
list = [] # inits list

k = int(input("Enter window size:")) # k input is made into an integer

for line in infile: # loops over lines
    
    line = line.strip("\n").split(",") # creates a list of the two strings in line
    year = line[0]
    temp = float(line[1])
    list.append(temp) # adds temp to list

index = k
outfile = open("MovingAve.csv", "w") # opens file to write
outfile.write("Year,Value\n") # prints header

for index in range(k, len(list) - k): # loops to wite moving avg
    year = 1880 + index
    avg = sum(list[index-k:index+k+1]) / (2*k+1)  # averages from a sum of range list[a:b]
    outfile.write(f"{year},{avg:.4f}\n") # writes output to file and formats avg to 4 decimal places
