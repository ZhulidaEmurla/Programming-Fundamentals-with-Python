ban_list = input().split(", ")
text = input()

for word in ban_list:
    replacement = '*' * len(word)
    text = text.replace(word, replacement)

print(text)
