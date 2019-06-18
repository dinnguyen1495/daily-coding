# Daily Coding 34
# Given a string, find the palindrome that can be made by inserting the fewest
# number of characters as possible anywhere in the word. If there is more than
# one palindrome of minimum length that can be made, return the lexicographically
# earliest one (the first one alphabetically).
# For example, given the string "race", you should return "ecarace", since we can
# add three letters to it (which is the smallest amount to make a palindrome).
# There are seven other palindromes that can be made from "race" by adding three
# letters, but "ecarace" comes first alphabetically.
# As another example, given the string "google", you should return "elgoogle"

def is_palindrome(string):
    return string[::-1] == string

def nearest_palindrome(string):
    if is_palindrome(string):
        return string
    if string[0] == string[-1]:
        return string[0] + nearest_palindrome(string[1:-1]) + string[0]
    palindrome1 = string[0] + nearest_palindrome(string[1:]) + string[0]
    palindrome2 = string[-1] + nearest_palindrome(string[:-1]) + string[-1]
    if len(palindrome1) < len(palindrome2):
        return palindrome1
    elif len(palindrome1) > len(palindrome2):
        return palindrome2
    return palindrome1 if palindrome1 < palindrome2 else palindrome2

def main():
    print(nearest_palindrome('race'))
    print(nearest_palindrome('google'))
    print(nearest_palindrome('NaN'))
    print(nearest_palindrome('water'))
    print(nearest_palindrome('elise'))

if __name__ == '__main__':
    main()