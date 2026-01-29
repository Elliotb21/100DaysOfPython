from prettytable import PrettyTable

table = PrettyTable()
table.field_names = ["Pokemon", "Type"]
table.add_rows([ 
                ["Pikachu", "Electic"],
                ["Squirtle", "Water"],
                ["Charmander", "Fire"],
                ])
table.align["Pokemon"] = "r"
table.align["Type"] = "l"
print(table)