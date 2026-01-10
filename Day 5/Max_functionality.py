# This program should replicate the max function without calling max.

student_scores = [180, 124, 165, 173, 189, 169, 146]
print(sum(student_scores))
print(max(student_scores))
print("-----")

# These do the same thing with a for loop but take more lines of code to view
sum = 0
for score in student_scores:
    sum += score
print(sum)

max = 0
for score in student_scores:
    if max < score:
        max = score
print(max)