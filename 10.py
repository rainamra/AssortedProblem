#10
def pangram (stnc:str):
    alphabet = "qwertyuiopasdfghjklzxcvbnm"
    for i in alphabet:
        if i not in stnc.lower():
            return False
    return True
print(pangram("The quick brown fox jumps over the lazy dog"))
