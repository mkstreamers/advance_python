#6. Convert a mixed-type tuple to a list, remove integers less than 10, and convert back to a tuple.
words = ["hello world", "madam", "python", "level", "code"]

sorted_words = sorted(words, key=len)

palindromes = [word for word in words if word == word[::-1]]

replaced = [word.replace(" ", "-") for word in words]

print("Sorted by length:", sorted_words)
print("Palindromes:", palindromes)
print("Spaces replaced:", replaced)