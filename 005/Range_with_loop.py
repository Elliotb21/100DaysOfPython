# Add up all the numbers from 1 to 100 using a range function in conjunction with a for loop
# Should total 5050 because 1 + 100 = 101, 2 + 99 = 101, etc. 50 times this occurs in the range 1 to 100
# So 50 * 101 = 5050


sum = 0
for num in range(1,101,1):
    sum += num
print(sum)