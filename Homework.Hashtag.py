import string

hashtag = input("Enter any phrase: ")
a = len(hashtag)
hashtag = hashtag.title()
hashtag1 = hashtag

for i in range(a):
    if hashtag[i] in string.punctuation or hashtag[i] in " ":
        hashtag1 = hashtag1.replace(hashtag[i], "")
hashtag2 = f"#{hashtag1[:140]}"
print(hashtag2)


