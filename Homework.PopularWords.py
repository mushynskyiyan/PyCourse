def popular_words(text, words):
    dict_words = {}
    swords = []
    for j in range(len(words)):
        swords.append(words[j].lower())
    text = text.lower().split()
    for i in swords:
        dict_words.setdefault(i, 0)
        for key in dict_words.keys():
            dict_words[key] = text.count(key)
    return dict_words


a = popular_words('''When I was One I had just begun When I was Two I was nearly new''',
                  ['i', 'was', 'three', 'near'])
print(a)
