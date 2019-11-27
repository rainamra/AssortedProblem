#2
def translate (stnc:str):
    vowel = "aiueo "
    stnc = list(stnc)
    for i in stnc:
        if i not in vowel:
            stnc[stnc.index(i)] = i + 'o' + i
    return (''.join(stnc))

print(translate("this is fun"))