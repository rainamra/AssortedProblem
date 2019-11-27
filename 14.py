#14
def makeForming(verb:str):
    consonant = "qwrtypsdfghjklzxcvbnm"
    vowel = "aiueo"
    exception = ["be", "see", "flee", "knee"]
    if verb[-2:] == "ie":
        return verb[:-2] + "ying"
    elif verb in exception:
        return verb + "ing"
    elif verb[-1] == "e" and verb not in exception:
        return verb[:-1] + "ing"
    elif verb[0] and verb[-1] in consonant and verb[1] in vowel:
        return verb + verb[-1] + "ing"
print(makeForming("run"))
print(makeForming("hug"))
print(makeForming("see"))
print(makeForming("move"))
print(makeForming("lie"))


