# Caesar Cipher is an encryption mechanism that shifts the English alphabet to encode and decode a particular message.

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l','m', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
cipher_running = True

def gather_information():
    direction = input("Type 'encode' to encrypt, and 'decode' to decrypt.\n").lower()
    text = input("Type your message. \n").lower()
    shift = int(input("Type the shift number: \n"))
    return direction, text, shift

def caesar_cipher(direction, text, shift):
    
    # Improved by merging encrypt & decrypt functions into one function called 'transform'   
    def transform(text, shift):
        result = ""
        for letter in text:
            if letter in alphabet:
                index = (alphabet.index(letter) + shift) % len(alphabet)
                result += alphabet[index]
            else:
                result += letter
        return result
    
    if direction == 'encode':
        print("your encoded text is: ", transform(text, shift))
    elif direction == 'decode':
        print("your decoded text is: ", transform(text, -shift))
    else:
        print("Please type 'encode' or 'decode' to operate the cipher. ")
        
while True:
    (direction, text, shift) = gather_information()
    caesar_cipher(direction, text, shift)
    
    keep_running = input("Keep going? (y/n): ").lower()
    if keep_running == "n":
        print("Thanks for using Caesar's cipher! Keep your wits about you...")
        break