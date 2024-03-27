words = ["dog", "talent", "loop", "aria", "tent", "choice"]
same_letter_words = []

for word in words:
    if word[0] == word[-1]:
        same_letter_words.append(word)

print("Words which starts and end with same letter are:")
for word in same_letter_words:
    print(word)
