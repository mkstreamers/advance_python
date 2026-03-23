#4. Create a student marks dictionary, then add, update, delete entries, and display keys, values, and items.
students = {"Alice": 85, "Bob": 90, "Charlie": 78}

students["David"] = 88
students["Alice"] = 95
del students["Charlie"]

print("Keys:", students.keys())
print("Values:", students.values())
print("Items:", students.items())