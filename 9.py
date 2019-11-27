#9
def filter_long_words(lwords:list, number:int):
    newList = []
    for i in range(len(lwords)):
        if (len(lwords[i])) >= number:
            newList.append(lwords[i])
    return newList
print(filter_long_words(["chirsty","raina","ali","cen"], 4))