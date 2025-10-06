"""
# PALINDROME CHECKER

print("PALINDROME CHECKER")

def is_palindrome(text):
    #remove spaces and make lower case
    new_text = text.replace(" ", "").lower()
    #check if text is equal to the reverse
    return new_text == new_text[::-1]

#get input from the user
word = input("Enter a word>> ")

#check if word is a palindrome
if is_palindrome(word):
    print(f"'{word}' is a palindrome")
else:
    print(f"'{word}' is not a palindrome")
"""

"""
# ANAGRAM CHECKER
print("ANAGRAM CHECKER")

def is_anagram(word1, word2):
    #remove space and make lower case
    word1 = word1.replace(" ", "").lower()
    word2 = word2.replace(" ", "").lower()

    #check if its an anagram
    return sorted(word1) == sorted(word2)

#user input
wd1 = input("Enter the first word>> ")
wd2 = input("Enter the second word>> ")

if is_anagram(wd1, wd2):
    print(f"'{wd1}' and '{wd2}' are anagrams")
else:
    print(f"'{wd1}' and '{wd2}' are not anagrams")
"""