# Daily Coding 37
# The power set of a set is the set of all its subsets. Write a function that, given a set,
# generates its power set.
# For example, given the set {1, 2, 3}, it should return {{}, {1}, {2}, {3}, {1, 2}, {1, 3}, {2, 3},
# {1, 2, 3}}.
# You may also use a list or array to represent a set.

from itertools import combinations

def power_set(input_set):
    return sum([list(map(list, combinations(input_set, i))) for i in range(0, len(input_set) + 1)], [])

def main():
    print(list(power_set({1, 2, 3})))

if __name__ == '__main__':
    main()