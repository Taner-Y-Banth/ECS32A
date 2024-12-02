# # # # k = int(input("Enter an integer:"))
# # # temps = [0.0, 51, 52, 23, 61, 25.4, -2.2, -5712.242, -582.25, 59]
# # # # for i in range(k, len(temps) - k + 1):
# # # #     print(temps[i])

# # # min_temp = None
# # # min_index = None
# # # for i in range(len(temps)):
# # #     if min_temp == None or temps[i] < min_temp:
# # #         min_temp = temps[i]
# # #         min_index = i
        
# # # print(min_temp, min_index)

# # pets = ['spam', 'cat', 'parrot', 'goldfish', 'dog']
# # pets.pop(0)
# # print(pets)

# def open_file():
#     while True:
#         try:
#             inp = input("Enter filename:")
#             infile = open(inp, "r")
#             print(infile.name)
#             return infile
#         except:
#             continue
        
# open_file()
    
def union(D1,D2):
    # print keys in D1 not in D2
    for key in D1:
            print(key)
    # print keys in D2 not in D1
    for key in D2:
        if key not in D1:
            print(key)

counts1 = {"A":1, "Alice":2, "Cat":3}
counts2 = {"A":1, "Romeo":2, "Cat":3}
union(counts1,counts2)