import json
import string 
import sys

with open("dictionary.json", "r") as file:
    ideologies = json.load(file)

print("Write in a phrase:")
phrase = input()
phrase = phrase.lower()

new_phrase = ""

for char in phrase:
    if char not in string.punctuation:
        new_phrase += char

words = new_phrase.split()

scores = {ideology: 0 for ideology in ideologies}

for word in words:
    for ideology in ideologies:
        if word in ideologies[ideology]:
            scores[ideology] += 1

best = max(scores, key=scores.get)
print("")
print(f"The best match for that phrase is {best}")

print("")
print("Do you want to see the full list of scores? Y/N")
opt = input()

if opt == "Y" or "y":
    for i in scores:
        print(f"Score for {(i)}: {scores[i]}")
else:
    sys.exit()