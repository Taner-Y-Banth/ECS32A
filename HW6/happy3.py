# happy3.py
# Ethan Bryant HW6
# ECS32A Dr. Kristian Stevens
# Adds search



def main():

    # Part 1
    # Build dictionary mapping countries to happiness index
    happy_dict = make_happy_dict()

    # Part 2
    # # Print key value pairs sorted by key
    # print_sorted_dictionary(happy_dict)

    # Part 3
    # Uncomment the function call below for part 3 only
    # lookup happiness by country until the user enters done
    lookup_happiness_by_country(happy_dict)

    # Parts 4-6
    # Uncomment the function call below for parts 4-6 
    # Read file containing population and GDP data and add happiness data
    #read_gdp_data(happy_dict)



def make_happy_dict():
    
    # inits dictionary
    dict = {}
    
    infile = open("happiness.csv", "r")
    infile.readline() # skips header

    # iterates over the lines and prints output of what will be made into a dictionary
    for line in infile:
        line = line.strip("\n").split(",") # makes list of the 3 variables
        dict[line[0]] = line[2] # adds item to dictionary
        # print(f"{line[0]} {line[2]}")

    # returns dictionary
    return dict

def read_gdp_data(happy_dict):
    return

def lookup_happiness_by_country(happy_dict):
    
    while True:
        try:
            inp = input("Enter a country to lookup or 'done' to exit:")
            if inp.lower() != "done":
              print(happy_dict[inp])
            else:
              break
        except:
            print(f"{inp} not found")
    
    return

# Function prints all the values in a dictionary d sorted by key
def print_sorted_dictionary(D):
    if type(D) != type({}):
        print("Dictionary not found")
        return
    print("Contents of dictionary sorted by key.")
    print("Key","Value")
    for key in sorted(D.keys()):
        print(key, D[key])
        
main()
