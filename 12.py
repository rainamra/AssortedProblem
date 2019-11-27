#12
import string
def caesar_cipher (text:str):
    alphabet = string.ascii_lowercase
    newWord = ""
    for i in text:
        next = alphabet.find(i) + 3
        if next > 26:
            next = next - 26
        newLetter = alphabet[next]
        newWord = newWord + newLetter
    return newWord
print(caesar_cipher("hey"))