from prettytable import PrettyTable
class User:
    def __init__(self, user_id, username):
        self.id = user_id
        self.username = username
        self.follower_count = 0
        self.following_count = 0
    
    def follow(self, user):
        """Adds 1 to specified user's (parameter) follower_count. Adds 1 to own following_count"""
        user.follower_count += 1
        self.following_count += 1  
    
    
user_1 = User(87792, "Elliot")
user_2 = User(94379, "Javier")

table = PrettyTable()
table.add_column("User 1", [user_1.id,user_1.username,user_1.follower_count, user_1.following_count])
table.add_column("User 2", [user_2.id,user_2.username,user_2.follower_count, user_2.following_count])
table.align["User 1"] = "l"
table.align["User 2"] = "r"
print(table)

user_1.follow(user_2)
table.add_column("User 1", [user_1.id,user_1.username,user_1.follower_count, user_1.following_count])
table.add_column("User 2", [user_2.id,user_2.username,user_2.follower_count, user_2.following_count])
print(table)