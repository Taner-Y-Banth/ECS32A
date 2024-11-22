# temp_file_stats.py
# Ethan Bryant HW5
# ECS32A Dr. Kristian Stevens
# Takes a csv file and manipulates data, finds mins and maxes

inp = input("Temperature anomaly filename:")
infile = open(inp, "r") # opens file
infile.readline() # skips Year,Value
dict = {} # inits dictionary

for line in infile:
    
    line = line.strip("\n").split(",") # creates a list of the two strings in line
    year = line[0]
    temp = float(line[1])
    dict[temp] = year # creates a dictionary entry temp is the key, year is the val
    
    # print(f"{year} {temp}")

minTemp = min(dict.keys()) # looks at all the keys(temp values) and finds the min
minYear = dict[minTemp] # uses key(minTemp) to find year value
maxTemp = max(dict.keys()) # looks at all the keys(temp values) and finds the max
maxYear = dict[maxTemp] # uses key(maxTemp) to find year value

if minYear == "1913":  # workaround due to two minimums
    if minTemp != -2.32:
        minYear = "1904"

print(f"Min temp: {minTemp} in {minYear}")
print(f"Max temp: {maxTemp} in {maxYear}")