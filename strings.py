import random


# Checking if string is palindrome:
def is_palindrome(text):
    count = 0
    reverse = text[::-1]
    for i in range(0, len(text)):
        if text[i] == reverse[i]:
            count += 1
    if count == len(text):
        return "palindrome"
    else:
        return "not palindrome"


# Longest word in a sequence:
def longest_word(text):
    words = text.split()
    max = 0
    result = ""
    for word in words:
        if len(word) > max:
            max = len(word)
            result = word
    return result


# Check if two strings are anagrams of each other:
def anagrams(text1, text2):
    counter = 0
    if len(text2) == len(text1):
        for i in text1:
            if i in text2:
                counter += 1
        if counter == len(text1):
            return "YES"
        else:
            return "NO"
    else:
        return "NO"


# Reverse a string:
def reverse_string(text):
    new_text = text[::-1]
    return new_text


# Find the most common word in a phrase:
def most_common_word(text):
    words = text.split()
    max = 0
    for word in words:
        if words.count(word) > max:
            max = words.count(word)
            result = word

    return result


# Generate a random password:
def password_generator(n):
    chars = ["a", "b", "c", "x", "y", "z", "w", "*", "@", "$", "1", "2", "3", "4", "5", "6", "7", "8", "9", "0"]
    password = ""
    for i in range(n):
        password += random.choice(chars)
    return password

print(is_palindrome("kayak"))
print(longest_word("Robert are pere"))
print(anagrams("ana", "naa"))
print(reverse_string("caine"))
print(most_common_word(" HEllo, eu sunt Robert numele meu este Robert eu robert"))
print(password_generator(10))
