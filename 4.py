#4
def is_member(char:str, list: [str]):
    for i in list:
        if char == i:
            return True
    return False
print(is_member("a", ["c", "b", "d"]))
print(is_member("d", ["c", "b", "d"]))