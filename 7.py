#7
def string_to_int (list:[str]):
    intList : [int] = []
    for i in list:
        intList.append(len(i))
    return intList
print(string_to_int(["aaa", "ccc"]))