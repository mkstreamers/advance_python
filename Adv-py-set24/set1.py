#1. What will be the output?
import numbers


x = [1,2,3]
print(x * 2)
#(a) [1,2,3,1,2,3]
#2. What is the output?
print(bool(""))
#(a) False
#3. Which is mutable?
#(a) List
#4. What will be output?
print(10 == 10.0)
#(a) True

#SECTION B: Output Prediction

#5 
a = [1,2,3]
b = a
b.append(4)
print(a)
#OUTPUT: [1, 2, 3, 4]
#6. What will be the output?
def func(x=[]):
    x.append(1)
    return x
print(func())
print(func())
#OUTPUT: [1]
#[1, 1]
#7. What will be the output?
for i in range(5):
    if i == 3:
        break
    print(i)
#OUTPUT: 0
#        1
#        2
#8. What will be the output?
try:
    print(10/0)
except:
    print("Error")
finally:
    print("Done")
#OUTPUT: Error
#        Done       

#SECTION C: Coding Questions

#9. Write a program to:
#   - Take input string
#   - Count vowels and consonants
def count_vowels_consonants(s):
    vowels = 'aeiouAEIOU'
    vowel_count = 0
    consonant_count = 0
    
    for char in s:
        if char.isalpha():
            if char in vowels:
                vowel_count += 1
            else:
                consonant_count += 1
                
    return vowel_count, consonant_count
input_string = input("Enter a string: ")
vowels, consonants = count_vowels_consonants(input_string)
print(f"Vowels: {vowels}")
print(f"Consonants: {consonants}")
#OUTPUT: Enter a string: Hello World
#        Vowels: 3
#        Consonants: 7

#10. Write a program to:
#   - Read a file
#   - Count number of lines, words and characters
def count_file_stats(filename):
    with open(filename, 'r') as file:
        lines = 0
        words = 0
        characters = 0
        for line in file:
            lines += 1
            words += len(line.split())
            characters += len(line)
    return lines, words, characters

filename = input("Enter the filename: ")
lines, words, characters = count_file_stats(filename)
print(f"Lines: {lines}")
print(f"Words: {words}")
print(f"Characters: {characters}")
#OUTPUT: Enter the filename: sample.txt
#        Lines: 10
#        Words: 50
#        Characters: 300
#11. Write a program:
#   - Create a class BankAccount
#   - Methods: deposit, withdraw, check balance
class BankAccount:
    def __init__(self):
        self.balance = 0
        
    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            print(f"Deposited: {amount}")
        else:
            print("Invalid deposit amount")
    
    def withdraw(self, amount):
        if amount > self.balance:
            print("Insufficient funds")
        elif amount <= 0:
            print("Invalid withdrawal amount")
        else:
            self.balance -= amount
            print(f"Withdrew: {amount}")
    
    def check_balance(self):
        print(f"Current balance: {self.balance}")
account = BankAccount()
account.deposit(100)
account.withdraw(30)
account.check_balance()
#        Deposited: 100
#        Withdrew: 30
#        Current balance: 70
#12. Write a program:
#   - Accept list of numbers
#   - Remove duplicates
#   - Sort it without using sort()
def remove_duplicates_and_sort(lst):
    unique_numbers = set(lst)
    sorted_numbers = sorted(unique_numbers)
    return sorted_numbers
input_list = list(map(int, input("Enter numbers separated by space: ").split()))
result = remove_duplicates_and_sort(input_list)
print("Sorted unique numbers:", result)
#OUTPUT: Enter numbers separated by space: 5 3 8 1 5
#        Sorted unique numbers: [1, 3, 5, 8]
#13.Write a program using lambda + map + filter:
#   - Square only even numbers from list
numbers = list(map(int, input("Enter numbers separated by space: ").split()))
squared_evens = list(map(lambda x: x**2, filter(lambda x: x % 2 == 0, numbers)))
print("Squared even numbers:", squared_evens)
#OUTPUT: Enter numbers separated by space: 1 2 3 4 5
#        Squared even numbers: [4, 16]      

#SECTION D: Advanced / Thinking

#16. Write a program:
#   - Simulate login system
#   - Use file to store username/password
def register():
    username = input("Enter a username: ")
    password = input("Enter a password: ")
    with open("users.txt", "a") as file:
        file.write(f"{username}:{password}\n")
    print("Registration successful!")

def login():
    username = input("Enter your username: ")
    password = input("Enter your password: ")
    with open("users.txt", "r") as file:
        for line in file:
            stored_username, stored_password = line.strip().split(":")
            if username == stored_username and password == stored_password:
                print("Login successful!")
                return
    print("Invalid username or password.")
register()
#        Enter a username: user1
#        Enter a password: pass1    
#        Registration successful!
login()
#        Enter your username: user1
#        Enter your password: pass1
#        Login successful!

#17. Exception Handling:
#- Create custom exception "InvalidAgeError"
#- Raise error if age < 18
class InvalidAgeError(Exception):
    pass

def check_age(age):
    if age < 18:
        raise InvalidAgeError("Age must be at least 18")
    print("Age is valid")
try:
    age = int(input("Enter your age: "))
    check_age(age)
except InvalidAgeError as e:
    print(e)
#OUTPUT: Enter your age: 16
#        Age must be at least 18    

# SECTION D: Advanced / Thinking

#19. Python + SQL:
#- Connect database
#- Create table Student
#- Insert 3 records
#- Fetch and display all records
import sqlite3
conn = sqlite3.connect('students.db')
cursor = conn.cursor()
cursor.execute('''CREATE TABLE IF NOT EXISTS Student
                  (id INTEGER PRIMARY KEY, name TEXT, age INTEGER)''')
students = [(1, 'Alice', 20), (2, 'Bob',    22), (3, 'Charlie', 19)]
cursor.executemany('INSERT INTO Student VALUES (?, ?, ?)', students)
conn.commit()
cursor.execute('SELECT * FROM Student')
records = cursor.fetchall()
for record in records:
    print(record)
conn.close()
#OUTPUT: (1, 'Alice', 20)
#        (2, 'Bob', 22)
#        (3, 'Charlie', 19)



