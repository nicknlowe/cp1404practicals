"""
CP1404/CP5632 Practical
Count the number of word occurrences in a string
Estimate: 20 minutes
Actual:   17 minutes
"""

word_to_count = {}
text = input("Text: ")
words = text.split()
for word in words:
    try:
        word_to_count[word] += 1
    except KeyError:
        word_to_count[word] = 1

words = list(word_to_count.keys())
words.sort()

for word in words:
    print(f"{word:{max((len(word) for word in words))}} : {word_to_count[word]}")
