paragraph= input().lower()
vowels = "aeiou"
prepositions = ["a", "an", "the", "in", "on", "at", "to", "for", "with", "by", "of", "from", "about", "as", "into", "over", "under", "between", "through", "during", "before", "after", "above", "below", "across", "against", "along", "around", "behind", "beside", "beyond", "but", "except"]
vowel_count = {}
preposition_count = {}
'''
for word in paragraph.split():
    if word in prepositions:
        preposition_count[word] = preposition_count.get(word, 0) + 1
'''
for prep in prepositions:
    if prep in paragraph:
        preposition_count[prep] =  paragraph.count(prep)
for char in vowels:
    vowel_count[char] = paragraph.count(char)

print("Preposition counts:")
for x,y in preposition_count.items():
    print(f"{x} : {y}")
print("\nVowel counts:")
for x, y in vowel_count.items():
    print(f"{x} : {y}")
