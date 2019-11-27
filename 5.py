#5
def overlapping (list1 : [str], list2 : [str]):
    for i in list1:
        for j in list2:
            if i == j:
                return True
    return False
print(overlapping(["r", "g", "i"], ["p", "j", "r"]))
print(overlapping(["r", "g", "i"], ["p", "j", "d"]))