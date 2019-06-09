# Daily Coding 2
# Given an array of integers, 
# return a new array such that each element 
# at index i of the new array is the product of all the numbers in the
# original array except the one at i.

def without_elem_product(arr):
    from functools import reduce
    result = []
    for i in range(len(arr)):
        result.append(reduce(lambda x, y: x * y, arr[:i] + arr[i + 1:], 1))
    return result 

def main():
    print(without_elem_product([1, 2, 3, 4, 5])) 

if __name__ == "__main__":
    main()