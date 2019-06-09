# Daily Coding 27
# Given a string of round, curly, and square open and closing brackets, return whether the brackets are
# balanced (well-formed).
# For example, given the string "([])[]({})", you should return true.
# Given the string "([)]" or "((()", you should return false.

def is_balanced(brackets):
    valid_brackets = {"(" : ")", "[" : "]", "{" : "}"}
    stack = []
    for bracket in brackets:
        if bracket in valid_brackets.keys():
            stack.append(bracket)
        elif valid_brackets[stack[-1]] == bracket:
            stack.pop(-1)
        else:
            return False
    return len(stack) == 0

def main():
    list = ["([])[]({})", "([)]", "((()"]
    for brackets in list:
        print("\"{0}\" is {1}balanced".format(brackets, "not " if not is_balanced(brackets) else ""))

if __name__ == "__main__":
    main()