#8
def find_longest_word (lword:[str]):
    longest_word : [int] = []
    for i in lword:
        longest_word.append((len(i),i))
        longest_word.sort()
    return longest_word [-1]
print(find_longest_word(["hey", "halo", "bye"]))