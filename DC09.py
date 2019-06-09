# Daily Coding 9
# Given a list of integers, write a function that returns the 
# largest sum of non-adjacent numbers. Numbers can be 0 or negative.

def maxNonAdjacentSum(array):
    inclusive_sum = 0
    exclusive_sum = 0

    for value in array:
        new_exclusive_sum = max(inclusive_sum, exclusive_sum)
        inclusive_sum = exclusive_sum + value
        exclusive_sum = new_exclusive_sum
    return max(inclusive_sum, exclusive_sum)

def main():
    array = [5, 1, 1, 5]
    print("Max sum without any 2 adjacent items:", maxNonAdjacentSum(array))

if __name__ == "__main__":
    main()