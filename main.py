import string

ideologies = {
    "Liberalism": ["freedom", "rights", "democracy", "market", "individual", "equality", "liberty", "diversity"],
    "Socialism": ["workers", "redistribution", "equality", "public ownership", "state control", "collective", "social justice", "regulate"],
    "Fascism": ["nation", "discipline", "order", "purity", "leader", "unity", "strength"],
    "Communism": ["class struggle", "proletariat", "revolution", "state ownership", "abolish property", "equality of outcome", "means of production"]
}

print("Write in a phrase:")
phrase = input()
phrase = phrase.lower()

new_phrase = ""

for char in phrase:
    if char not in string.punctuation:
        new_phrase += char

words = new_phrase.split()

scores = {
    "Liberalism": 0,
    "Socialism": 0,
    "Fascism": 0,
    "Communism": 0,
}

for word in words:
    for ideology in ideologies:
        if word in ideologies[ideology]:
            scores[ideology] += 1

best = max(scores, key=scores.get)
print(f"The best match for that phrase is {best}")