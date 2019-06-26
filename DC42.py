# Daily Coding 42
# Given a list of integers S and a target number k, write a function that returns a subset of S that
# adds up to k. If such a subset cannot be made, then return null.
# Integers can appear more than once in the list. You may assume all numbers in the list are
# positive.
# For example, given S = [12, 1, 61, 5, 9, 2] and k = 24, return [12, 9, 2, 1] since it sums up to
# 24.

def subset_sum(integers, k):
    if k <= 0:
        return []
    for i in range(len(integers)):
        if integers[i] > k:
            continue
        temp = [integers[i]] + subset_sum(integers[:i] + integers[i + 1:], k - integers[i])
        if sum(temp) == k:
            return temp
    return []

def main():
    print(subset_sum([12, 1, 61, 5, 9, 2], 24))

if __name__ == '__main__':
    main()