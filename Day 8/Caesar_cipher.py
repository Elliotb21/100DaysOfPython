# Caesar Cipher is an encryption mechanism that shifts the phonetic alphabet to encode and decode a particular message.

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l','m', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

direction = input("Type 'encode' to encrypt, and 'decode' to decrypt.\n").lower()
text = input("Type your message. \n").lower()
shift = int(input("Type the shift number: \n"))
cipher_running = True

def caesar_cipher(original_text, shift_amount):

    def encrypt(original_text, shift_amount): 
        cipher_text = ""
        for letter in original_text:
            shifted_index = alphabet.index(letter) + shift_amount
            shifted_index %= len(alphabet)
            cipher_text += alphabet[shifted_index]
        print(f"Your encoded text is {cipher_text}.")
                       
    def decrypt(original_text, shift_amount):
        plain_text = ""
        for letter in original_text:
            shifted_index = alphabet.index(letter) - shift_amount
            shifted_index %= len(alphabet)
            plain_text += alphabet[shifted_index]
        print(f"Your decoded text is {plain_text}.")
    
    if direction == 'encode':
        encrypt(text, shift)
    elif direction == 'decode':
        decrypt(text, shift)
    else:
        print("Please type 'encode' or 'decode' to operate the cipher. ")
        
while cipher_running:
    caesar_cipher(text, shift)
    keep_running = input("Keep going? (y/n): ").lower()
    if keep_running == "y":
        direction = input("Type 'encode' to encrypt, and 'decode' to decrypt.\n").lower()
        text = input("Type your message. \n").lower()
        shift = int(input("Type the shift number: \n"))
    elif keep_running == "n":
        print("Thanks for using Caesar's cipher! Keep your wits about you...")
        cipher_running = False
    else: 
        print("Not a valid selection, continuing program.")