#Final project for Day 2

print("Welcome to the tip calculator!")
#Information gathering from user
total = float(input("What was the total bill?  $") )
tip = int(input("What tip percentage do you want to give? (10%, 12%, or 15%)  "))
party_size = int(input("How many people are splitting the bill?  "))

#Mathematical operations
tip_conversion = 1 + (tip / 100)
total_with_tip = (total * tip_conversion)
total_with_party = total_with_tip / party_size
rounded_total = round(total_with_party, 2)

#Output
print(f"Each person should pay: ${rounded_total}\n")
