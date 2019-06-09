# Daily Coding 0
# Given an array of integers, find the first missing positive integer in linear time and constant space. 
# In other words, find the lowest positive integer that does not exist in the array. The array can
# contain duplicates and negative numbers
# For example, the input [3, 4, -1, 1] should give 2. The input [1, 2, 0] should give 3.

def lowest_positive_integer(arr):
    result = 1
    i = 0
    while i < len(arr):
        if result == arr[i]:
            result += 1
            i = 0
        i += 1
    return result

def main():
    test_1 = [1, 2, 0]
    test_2 = [3, 4, -1, 1]
    print("First missing positive integer for", test_1, ":", lowest_positive_integer(test_1))
    print("First missing positive integer for", test_2, ":", lowest_positive_integer(test_2))

if __name__ == "__main__":
    main()