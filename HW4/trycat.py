# trycat.py
# Ethan Bryant HW4
# ECS32A Dr. Kristian Stevens
# Was demonstrated in lecture, prints lines, with error checking

# file opened for reading
while True:
    try:
        # input filename
        file_name = input("Enter a file name to open:")
        infile = open(file_name, "r")
        break
    except:
        print(f"Could not open '{file_name}'")
        continue
    

for line in infile:
# strip whitespace from ends
    line = line.strip()
    print(line)
