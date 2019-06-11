# Daily Coding 25
# Implement regular expression matching with the following special characters:
#   . (period) which matches any single character
#   * (asterisk) which matches zero or more of the preceding element
# That is, implement a function that takes in a string and a valid regular expression and returns whether
# or not the string matches the regular expression.
# For example, given the regular expression "ra." and the string "ray", your function should return true.
# The same regular expression on the string "raymond" should return false.
# Given the regular expression ".*at" and the string "chat", your function should return true. The same
# regular expression on the string "chats" should return false.
# Dynamic algorith's source: https://youtu.be/l3hda49XcDE

def match_regex(string, pattern):
    check = [[False] * (len(pattern) + 1) for _ in range(len(string) + 1)]
    check[0][0] = True

    for i in range(0, len(check)):
        for j in range(1, len(check[0])):
            if pattern[j - 1] in {string[i - 1], '.'}:
                check[i][j] = check[i - 1][j - 1]
            if pattern[j - 1] == '*':
                check[i][j] = check[i][j - 2] or (check[i - 1][j] if pattern[j - 2] in {string[i - 1], '.'} else False)
    return check[len(string)][len(pattern)]

def main():
    print(match_regex("xaabyc", "xa*b.c"))
    print(match_regex("chat", ".*at"))
    print(match_regex("lllt", ".*l*t"))
    print(match_regex("helloworld", ".h*d"))

if __name__ == '__main__':
    main()