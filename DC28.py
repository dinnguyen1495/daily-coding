# Daily Coding 28
# Write an algorithm to justify text. Given a sequence of words and an integer line length k, return a
# list of strings which represents each line, fully justified.
# More specifically, you should have as many words as possible in each line. There should be at least one
# space between each word. Pad extra spaces when necessary so that each line has exactly length k. Spaces
# should be distributed as equally as possible, with the extra spaces, if any, distributed starting from
# the left.
# If you can only fit one word on a line, then you should pad the right-hand side with spaces.
# Each word is guaranteed not to be longer than k.
# For example, given the list of words ["the", "quick", "brown", "fox", "jumps", "over", "the", "lazy", 
# "dog"] and k = 16, you should return the following:
# ["the  quick brown", # 1 extra space on the left
# "fox  jumps  over", # 2 extra spaces distributed evenly
# "the   lazy   dog"] # 4 extra spaces distributed evenly
# Dynamic algorithm's source: https://youtu.be/RORuwHiblPc
 
import math

def justify_text(words, k):
    N = len(words)

    # Create the cost matrix
    words_length = [len(word) for word in words]
    cost_matrix = [[-1] * N for _ in range(N)]
    for i in range(N):
        for j in range(N):
            if j >= i:
                temp = sum(words_length[i:j + 1]) + (j - i)
                cost_matrix[i][j] = (k - temp) ** 2 if temp <= k else math.inf

    # Compute minimum costs and marking positions
    min_cost, marking_positions = [-1] * N, [-1] * N
    j = N - 1
    for i in range(N - 1, -1, -1):
        if -1 < cost_matrix[i][j] < math.inf:
            min_cost[i] = cost_matrix[i][j]
            marking_positions[i] = j + 1
            continue
        cost = math.inf
        break_point = j
        for n in range(j, i, -1):
            if cost_matrix[i][n - 1] == math.inf:
                continue
            temp = cost_matrix[i][n - 1] + min_cost[n]
            if temp < cost:
                cost = temp
                break_point = n
        min_cost[i] = cost
        marking_positions[i] = break_point

    # Compute spaces between words in a line and output result
    result = []
    i = 0
    while i < N:
        limit = marking_positions[i]
        if limit - i == 1:
            temp = words[i] + (" " * (k - words_length[i]))
            result.append(temp)
        else:
            spaces = (k - sum(words_length[i:limit])) // (limit - i - 1)
            rest = (k - sum(words_length[i:limit])) % (limit - i - 1)
            if rest == 0:
                result.append(((" ") * spaces).join(words[i:limit]))
            else:
                result.append(words[i] + (" " * (spaces + rest)) + ((" ") * spaces).join(words[i + 1:limit]))
        i = limit
    return result

def main():
    words = ["the", "quick", "brown", "fox", "jumps", "over", "the", "lazy", "dog"]
    print(justify_text(words, 16))

if __name__ == "__main__":
    main()