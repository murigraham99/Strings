import random


# Checking if string is palindrome:
def ex6(text):
    count = 0
    reverse = text[::-1]
    for i in range(0, len(text)):
        if text[i] == reverse[i]:
            count += 1
    if count == len(text):
        print("Este palindrom")
    else:
        print("Nu este palindrom")


# Longest word in a sequence:
def ex7(text):
    words = text.split()
    max = 0
    result = ""
    for word in words:
        if len(word) > max:
            max = len(word)
            result = word
    print(result)


# Check if two strings are anagrams of each other:
def ex8(text1, text2):
    counter = 0
    if len(text2) == len(text1):
        for i in text1:
            if i in text2:
                counter += 1
        if counter == len(text1):
            print("YES")
        else:
            print("NO")
    else:
        print("NO")


# Reverse a string:
def ex11(text):
    new_text = text[::-1]
    print(new_text)


# Find the most common word in a phrase:
def ex19(text):
    words = text.split()
    max = 0
    for word in words:
        if words.count(word) > max:
            max = words.count(word)
            result = word

    print(f"Cuvant = {result}")


# Generate a random password:
def ex20(n):
    chars = ["a", "b", "c", "x", "y", "z", "w", "*", "@", "$", "1", "2", "3", "4", "5", "6", "7", "8", "9", "0"]
    password = ""
    for i in range(n):
        password += random.choice(chars)
    print(password)
