#TODO: Create a letter using starting_letter.txt 
#for each name in invited_names.txt
#Replace the [name] placeholder with the actual name.
#Save the letters in the folder "ReadyToSend".
    
#Hint1: This method will help you: https://www.w3schools.com/python/ref_file_readlines.asp
    #Hint2: This method will also help you: https://www.w3schools.com/python/ref_string_replace.asp
        #Hint3: THis method will help you: https://www.w3schools.com/python/ref_string_strip.asp
        
        
with open("./Input/Names/invited_names.txt", "r") as file:
    invited_names = [name.strip() for name in file.readlines()]
    
with open("./Input/Letters/starting_letter.txt", "r") as file:
    template = file.read()
    
for name in invited_names:
    personalized = template.replace("[name]", name)
    with open(f"./Output/ReadyToSend/{name}.txt", "w") as file:
        file.write(personalized)