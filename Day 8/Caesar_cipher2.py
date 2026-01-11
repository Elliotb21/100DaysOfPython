# Caesar Cipher is an encryption mechanism that shifts the phonetic alphabet to encode and decode a particular message.

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l','m', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
cipher_running = True

def gather_information():
    direction = input("Type 'encode' to encrypt, and 'decode' to decrypt.\n").lower()
    text = input("Type your message. \n").lower()
    shift = int(input("Type the shift number: \n"))
    return direction, text, shift

def caesar_cipher(direction, text, shift):

    def encrypt(text, shift): 
        cipher_text = ""
        for letter in text:
            if letter in alphabet:
                shifted_index = alphabet.index(letter) + shift
                shifted_index %= len(alphabet)
                cipher_text += alphabet[shifted_index]
            else:
                cipher_text += letter
        print(f"Your encoded text is {cipher_text}.")
                       
    def decrypt(text, shift):
        plain_text = ""
        for letter in text:
            if letter in alphabet:
                shifted_index = alphabet.index(letter) - shift
                shifted_index %= len(alphabet)
                plain_text += alphabet[shifted_index]
            else:
                plain_text += letter
        print(f"Your decoded text is {plain_text}.")
    
    if direction == 'encode':
        encrypt(text, shift)
    elif direction == 'decode':
        decrypt(text, shift)
    else:
        print("Please type 'encode' or 'decode' to operate the cipher. ")
        
while True:
    (direction, text, shift) = gather_information()
    caesar_cipher(direction, text, shift)
    
    keep_running = input("Keep going? (y/n): ").lower()
    if keep_running == "n":
        print("Thanks for using Caesar's cipher! Keep your wits about you...")
        break