# Daily Coding 33
# Compute the running median of a sequence of numbers. That is, given a stream of numbers, print out the median of the list so far on each new element.
# Recall that the median of an even-numbered list is the average of the two middle numbers.
# For example, given the sequence [2, 1, 5, 7, 2, 0, 5], your algorithm should print out:
# [2, 1.5, 2, 3.5, 2, 2, 2]

from statistics import median

def median_list(list):
    n, result = len(list), []
    for i in range(1, n + 1):
        sorted_list, quotient, rest = sorted(list[:i]), i // 2, i % 2
        result.append(sorted_list[quotient] if rest != 0 
            else sum(sorted_list[quotient - 1:quotient + 1]) / 2)
    return result

def main():
    print(median_list([2, 1, 5, 7, 2, 0, 5]))

if __name__ == "__main__":
    main()