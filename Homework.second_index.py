def second_index(word, letter):
    if word.count(letter) > 1:
        a = word.find(letter, word.find(letter) + 1)
    else:
        a = None
    return a


w = input("Enter word: ")
le = input("Enter letter or letters: ")
print(second_index(w, le))
