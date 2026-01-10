print('''
                                 d
                                d8
                               dP8
                              d8 8
                             d8P 8
                            d88  8
                           d88P  8
                          d888   8
                         d888P   8
                        d8888    8
                       d8888P    8
                      d88888     8
        oooood       d88888booooo8
       d8 8"""""Ybooooooooooooooo8oooooooooooooodP"""P""
       88 Y                                  cgmm .P"   
      d88  Y                                    .P"  
      888   YooooooooooooooooooooooooooooooooooP"  
      
      
      WELCOME TO TREASURE ISLAND!
      Your mission is to find the treasure
''')

direction = input("Do you want to go [L]eft or [R]ight? ")

if direction == "L":
      swim = input("Do you want to [S]wim or wait for a [B]oat? ")
      if swim == "S":
            print("Attacked by a Barracuda.\n\n...Game Over...")
      else:
            door = input("You arrive at 3 doors. Choose wisely...[R]ed, [B]lue, [Y]ellow... ")
            if door == "R":
                  print("Burned by fire.\n\n...Game Over...")
            elif door == "B":
                  print("Eaten by beasts.\n\n...Game Over...")
            elif door == "Y":
                  print("You win!")
            else: 
                  print("That was not an option. You have received the treasure. \n\n...Simulation Over...")
else:
      print("Fall into a hole.\n\n...Game Over...")

#print("You found the hidden treasure!")