#13
def makeForms(verbs:str):
    suffixes = ["o", "ch", "s", "sh", "x", "z"]
    if verbs[-1] == "y" :
        return verbs[:-1] + "ies"
    elif verbs[-1]in suffixes or verbs[-2:] in suffixes:
        return verbs + "es"
    else:
        return verbs + "s"

print(makeForms("run"))
print(makeForms("brush"))
print(makeForms("try"))
print(makeForms("fix"))



