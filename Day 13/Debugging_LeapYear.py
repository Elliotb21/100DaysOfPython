# Starting code
def is_leap(year):
    if year % 4 == 0:
        if year % 100 == 0:
            if year % 4000 == 0:
                return True
            else:
                return False
        else:
            return True
    else:
        return False
print(is_leap(8000))
# Didn't need to use the debugger for this one, we can see the comparison for the final if has an extra 0.
# Using the debugger you can set the value of year and if you set it to 2000 or a reasonable year, we can see where
# the comparison fails, on the final IF statement