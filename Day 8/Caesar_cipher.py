# Caesar Cipher is an encryption mechanism that shifts the phonetic alphabet to encode and decode a particular message.

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l','m', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

direction = input("Type 'encode' to encrypt, and 'decode' to decrypt.\n").lower()
text = input("Type your message. \n").lower()
shift = int(input("Type the shift number: \n"))

def encrypt(original_text, shift_amount):
    shifted_index = 0
    text_accumulator = ""
    for letter in original_text:
        shifted_index = alphabet.index(letter) + shift
        text_accumulator += alphabet[shifted_index]
    print(text_accumulator)
                
encrypt(text, 5)
        
    