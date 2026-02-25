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
print(data)
print(data["temp"])