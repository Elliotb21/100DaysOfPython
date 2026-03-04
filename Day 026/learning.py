#List comprehension!

# Syntax for list comprehension looks like below
# new_list = [new_item for item in list if test]

# list = [1,2,3]
# new_list =[num+1 for num in list]
# print(new_list) # prints [2,3,4]


# new_range = [num * 2 for num in range(1,10)]
# print(new_range) # prints [2,4,6,8,10,12,16,18]


# names = ["Alex", "Beth", "Caroline", "Dave", "Eleanor", "Freddie"]
# # short_names = [name for name in names if len(name) < 5] # Makes a new list with names shorter than 5 letters
# # print(short_names)
# uppercase_names_over_5 = [name.upper() for name in names if len(name) > 4]
# print(uppercase_names_over_5)

# Compares file1 and file2 and makes a new list with integers only in both lists.
# with open("file1.txt") as file1:
#     file1_list = [num.strip() for num in file1]
# with open("file2.txt") as file2:
#     file2_list = [num.strip() for num in file2]
    
# result = [int(num) for num in file1_list if num in file2_list]
# print(result)

# Better version O(n) instead of O(n**2)
# with open("file1.txt") as file1:
#     file1_set = {line.strip() for line in file1}
# with open("file2.txt") as file2:
#     file2_set = {line.strip() for line in file2}

# result = list(file1_set & file2_set)
# print(result)