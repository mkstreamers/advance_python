#13. Unique Character Extractor Input a sentence and print characters that appear only once. Ignore spaces and punctuation. Use sets and loops to identify uniqueness.
sentence = input("Enter a sentence: ")

unique_chars = set()
duplicates = set()

for char in sentence:
    if char.isalnum():
        if char in unique_chars:
            duplicates.add(char)
        else:
            unique_chars.add(char)

result = [char for char in unique_chars if char not in duplicates]

print("Unique characters:", result)