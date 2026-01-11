def life_in_weeks(age):  
    if 0 < age < 90:
        weeks_left = 52 * (90 - age)
    print(f"you have {weeks_left} weeks left.")

print("This programs takes your age and tells you how many weeks you have left if you live until 90.")  
age = int(input("How old are you? \n"))
life_in_weeks(age)
