#15. String Pattern Validator Input a string and check whether it’s a palindrome. Count total vowels, consonants, digits, and special characters using loops and conditions.
s = input("Enter a string: ")

vowels = "aeiouAEIOU"
v = c = d = sp = 0

for ch in s:
    if ch in vowels:
        v += 1
    elif ch.isalpha():
        c += 1
    elif ch.isdigit():
        d += 1
    else:
        sp += 1

is_palindrome = s == s[::-1]

print("Palindrome:", is_palindrome)
print("Vowels:", v)
print("Consonants:", c)
print("Digits:", d)
print("Special characters:", sp)