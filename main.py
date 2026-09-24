# Put any imports up here:
import random
import pyperclip
'''
Q1. Print out the 4th letter ("r") from the string name using bracket notation and the index.
Syntax: variable_name[index]
'''
name = "snorlax"
print("Q1. The 4th letter is:")
print(name[3])


'''
Q2. Strings are iterable, too! You can treat them like a list.
Print out a random character from the string letters using the random module and the choice() method.
https://www.w3schools.com/python/module_random.asp
'''
letters = "abcdefghijklmnopqrstuvwxyz"
print("\nQ2. A random letter is:")
print(random.choice(letters))


'''
Q3. Print out 5 random characters from letters using a for-loop.
'''
print("\nQ3. Five nights... I mean 5 random characters are:")
for i in range(5):
    print(random.choice(letters))




'''
Q5. Save 5 random characters to the string random_letters. Then, print out random_letters.
'''
random_letters = ""
print("\nQ5. random_letters:")
for i in range(5):
     random_letters += random.choice(letters)

print(random_letters)



'''
Q6. Look at Pyperclip and copy random_word to the computer's clipboard. You'll need to import and install it.
https://pypi.org/project/pyperclip/
'''
pyperclip.copy(random_letters)


# Check that the copy worked by pasting it here or printing it again: 

'''
Q7. Ask the user for a name and phone number and store them in the dictionary phone_book.
Notice the data types of the key-value pairs.
'''
phone_book = {
    "Jenny": "867-5309",
    "The Police": "911",
    "WTHS": "508-799-1940"
}

name = input("Enter your name: ")
phone = input(f"Enter {name}'s phone number: ")

#put name and phone in dictionary
phone_book[name] = phone
print(phone_book)
'''
Q8. Print out all the phone numbers with a for-loop in the format:
[name]'s phone number: [number]
https://www.w3schools.com/python/python_dictionaries_loop.asp
'''
print("\nMy Phone Book:")
for name,phone in phone_book.items():
     print(f"{name}'s phone number: {phone}")