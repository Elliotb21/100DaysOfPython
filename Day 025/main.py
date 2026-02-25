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
# #object attribute
# print(data.condition)
# #more like a dictionary.
# print(data["condition"])