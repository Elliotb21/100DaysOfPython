import csv
import pandas

# with open("./weather_data.csv") as file:
#     data = csv.reader(file)
    # temperatures = []
    # for row in data:
    #     if row[1] != "temp":
    #         temperatures.append(int(row[1]))
    # print(temperatures)
    
data = pandas.read_csv("./weather_data.csv")
# print(data)
# print(data["temp"])
# data_dict = data.to_dict()
# print(data_dict)

# print(data["temp"].mean())
# data_list = data["temp"].tolist()
# average = sum(data_list) / len(data_list)
# print(average)

# print(data["temp"].max())
# object attribute
# print(data.condition)
# more like a dictionary.
# print(data["condition"])

# print a row
# print(data[data.day == "Monday"])

# print a row where the temperature was at the maximum
# print(data[data.temp == data.temp.max()])

# print a value in a particular row
# monday = data[data.day == "Monday"]
# print(monday.condition)

# convert Monday's temperature from C to F
# f = (c * 1.8) + 32
# monday = data[data.day == "Monday"]
# ctemp = monday.temp[0]
# ftemp = ctemp * 9/5 + 32
# print(ftemp)

# Create a dataframe from data
# data_dict = {
#     "students": ["Amy", "James", "Angela"],
#     "scores": [76, 56, 65] 
# }
# data = pandas.DataFrame(data_dict)
# print(data) 

# # Create a csv from data! Only needs a path variable.
# data.to_csv("./data.csv")