#2. Process a user-entered sentence: count vowels/consonants, reverse it, replace spaces with underscores, capitalize words.
sentence = input("Enter a sentence: ")

vowels = "aeiouAEIOU"
vowel_count = 0
consonant_count = 0

for char in sentence:
    if char.isalpha():
        if char in vowels:
            vowel_count += 1
        else:
            consonant_count += 1

reversed_sentence = sentence[::-1]
underscore_sentence = sentence.replace(" ", "_")
capitalized_sentence = sentence.title()

print("Vowels:", vowel_count)
print("Consonants:", consonant_count)
print("Reversed Sentence:", reversed_sentence)
print("With underscores:", underscore_sentence)
print("Capitalized:", capitalized_sentence)