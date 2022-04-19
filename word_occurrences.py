dictionary = {}
text = input("Text: ").split()
for i in text:
    if i not in dictionary:
        dictionary[i] = 1
    else:
        dictionary[i] += 1
word_length = max(len(word) for word in dictionary)
for x, y in sorted(dictionary.items()):
    print(f"{x:<{word_length}} : {y}")

