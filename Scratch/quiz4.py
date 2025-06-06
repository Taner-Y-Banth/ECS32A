# total = "$100.00"
# total = total[1:]
# total = float(total)
# print(total)

# filename = input("CSV file:")
# infile = open(filename)
# filename = input("Output TSV file:")
# outfile = open(filename, "w")
# for line in infile:
#     line = line.rstrip("\n")
#     # replace comma with tab
#     line = line.replace(',', '\t')
#     # write output line to file
#     outfile.write(line)

# outfile.close()

# L = []
# for i in range(1,6):
#     L.append(float(i))
# print(L)

# infile = open("input.txt", "r")

# def names_match(a,b):
#     if a.lower() == b.lower():
#         result = True
#     else:
#         result = False
#     return result

# print(names_match("Alice", "ALICE"))
# print(names_match("Alice", "ALICE!"))

s = input("Enter an email:")
i = s.split("@")
print("Domain:",i[1])