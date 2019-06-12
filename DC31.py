# Daily Coding 31
# The edit distance between two strings refers to the minimum number of character
# insertions, deletions, and substitutions required to change one string to the
# other. For example, the edit distance between “kitten” and “sitting” is three:
# substitute the 'k' for 's', substitute the 'e' for 'i', and append a 'g'.
# Given two strings, compute the edit distance between them.
# Note: Levenshtein Distance

# Recursive Implementation
def levenshtein_distance_rec(str1, str2):
    if str1 == "":
        return len(str2)
    if str2 == "":
        return len(str1)
    if str1[-1] == str2[-1]:
        cost = 0
    else:
        cost = 1
    return min(levenshtein_distance_rec(str1[:-1], str2) + 1, levenshtein_distance_rec(str1, str2[:-1]) + 1, levenshtein_distance_rec(str1[:-1], str2[:-1]) + cost)

# Iterative Implementation using Dynamic Programming
def levenshtein_distance_iter(str1, str2):
    memo = [[0] * (len(str2) + 1) for _ in range(len(str1) + 1)]
    for i in range(len(memo)):
        memo[i][0] = i
    for j in range(len(memo[0])):
        memo[0][j] = j
    for i in range(1, len(memo)):
        for j in range(1, len(memo[i])):
            cost = 0
            if str1[i - 1] != str2[j - 1]:
                cost = 1
            memo[i][j] = min(memo[i - 1][j] + 1, memo[i][j - 1] + 1, memo[i - 1][j - 1] + cost)
    return memo[len(str1)][len(str2)]

def main():
    def test(str1, str2):
        print("Levenshtein distance between \"" + str1 + "\" and \"" + str2 + "\" is:", levenshtein_distance_iter(str1, str2))
    test('kitten', 'sitting')
    test('bicycle', 'tricycle')
    test('superman', 'batman')
    test('programmer', 'informatiker')
    test('Manhattan', 'Marathon')

if __name__ == "__main__":
    main()