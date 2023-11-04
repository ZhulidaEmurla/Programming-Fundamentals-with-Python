
words = input().split()


word_counts = {}


for word in words:
    word = word.lower()
    if word in word_counts:
        word_counts[word] += 1
    else:
        word_counts[word] = 1


for word, count in word_counts.items():
    if count % 2 != 0:
        print(word, end=" ")
