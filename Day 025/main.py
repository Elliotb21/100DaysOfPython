import pandas
import csv

# Goal is to take data from 2018 Central Park Squirrel file, import into project as dataframe,
# iterate through and increment counts for 3 distinct colors, then output to_csv fur color, count
# grey, red, black and their respective counts into a small table.

# Access the main data
squirrel_data = pandas.read_csv("../Resources/2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv")
# Access the column for Primary Fur Color and increment counts for each color
# for color in len(squirrel_data["Primary Fur Color"]):
#     if squirrel_data["Primary Fur Color"] == ""

squirrel_dict = {
    "fur_color":["gray", "red", "black"],
    "color_count":[0, 0, 0]
}
for color in squirrel_data["Primary Fur Color"]:
    if color == "Gray":
        squirrel_dict["color_count"][0]  += 1
    elif color == "Cinnamon":
        squirrel_dict["color_count"][1] += 1
    elif color == "Black":
        squirrel_dict["color_count"][2] += 1

squirrel_colors = pandas.DataFrame(squirrel_dict)
print(squirrel_colors)
squirrel_colors.to_csv("../Resources/squirrel_fur_color_counts.csv")
