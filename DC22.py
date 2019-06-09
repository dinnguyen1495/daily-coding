# Daily Coding 22
# Given a dictionary of words and a string made up of those words (no spaces), return the original
# sentence in a list. If there is more than one possible reconstruction, return any of them. If there is
# no possible reconstruction, then return null.
# For example, given the set of words 'quick', 'brown', 'the', 'fox', and the string "thequickbrownfox",
# you should return ['the', 'quick', 'brown', 'fox'].
# Given the set of words 'bed', 'bath', 'bedbath', 'and', 'beyond', and the string "bedbathandbeyond",
# return either ['bed', 'bath', 'and', 'beyond] or ['bedbath', 'and', 'beyond'].
# Note: for all possible combinations: use permutations from itertools!

def reconstructor(set, string):
    if len(set) == 0 or len(string) == 0:
        return None
    result = []
    temp = 0
    i = 1
    while temp < len(string) - 1 and i <= len(string):
        if string[temp:i] in set:
            result.append(string[temp:i])
            if i < len(string) - 1:
                temp = i
            else:
                break
        i += 1
    if len(''.join(result)) < len(string):
        return None
    return result

def compound_check(list, set):
    for i in range(2, len(list) + 1):
        for j in range(0, len(list) - i + 1):
            if ''.join(list[k] for k in range(j, j + i)) in set:
                list[j] = ''.join(list[k] for k in range(j, j + i))
                for k in range(j + 1, j + i):
                    list.remove(list[k])
                return list
    return None

def main():
    combi1 = reconstructor({'quick', 'brown', 'the', 'fox'}, "thequickbrownfox")
    print("List 1:", combi1)
    combi2 = reconstructor({'bed', 'bath', 'bedbath', 'and', 'beyond'}, "bedbathandbeyond")
    print("List 2:", combi2)
    print(compound_check(combi2, ({'bed', 'bath', 'bedbath', 'and', 'beyond'})))

if __name__ == "__main__":
    main()