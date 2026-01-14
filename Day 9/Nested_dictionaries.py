# Nesting a List inside a Dictionary
# Instead of a String value assigned to a key, we can replace it with a List.
# You can nest a List in a Dictionary like this:

# my_dictionary = {
#     key1: [List],
#     key2: Value,
# }

# See if you can figure out how to print out "Lille" from the nested List called travel_log.
# Now do Stuttgart
travel_log = {
    "France": ["Paris", "Lille", "Dijon"],
    "Germany": ["Stuttgart", "Berlin"],
}
print(travel_log["France"][1])
print(travel_log["Germany"][0])

# Nesting Lists inside other Lists
# We've previously seen Nested Lists:
# Do you remember how to get items that are nested deeply in a list? Try to print "D" from the list nested_list.
# Nesting a Dictionary inside a Dictionary
# You can also nest a dictionary in a dictionary:
nested_list = ["A", "B", ["C", "D"]]
print(nested_list[2][1])
# A, comma is index position 0
# my_dictionary = {
#     key1: Value,
#     key2: {Key: Value, Key: Value},
# }

# Figure out how to print out "Stuttgart" from the following list:
# Now do 12

travel_log = {
  "France": {
    "cities_visited": ["Paris", "Lille", "Dijon"], 
    "total_visits": 12
   },
  "Germany": {
    "cities_visited": ["Berlin", "Hamburg", "Stuttgart"], 
    "total_visits": 5
   },
}
print(travel_log["Germany"]["cities_visited"][2])
print(travel_log["France"]["total_visits"])
