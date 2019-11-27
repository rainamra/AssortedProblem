#11
def char_freq(letters:str):
    freq : str = ""
    while letters != "":
        freq = freq + letters[0] + " x " + str(letters.count(letters[0])) + "\n"
        letters = letters.replace(letters[0],"")
    return freq
print(char_freq("matahari"))