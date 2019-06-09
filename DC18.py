# Daily Coding 18
# Given an array of integers and a number k, where 1 <= k <= length of the array, compute the maximum
# values of each subarray of length k.
# For example, given array = [10, 5, 2, 7, 8, 7] and k = 3 , we should get: [10, 7, 8, 8], since:
# 10 = max(10, 5, 2) 
# 7 = max(5, 2, 7) 
# 8 = max(2, 7, 8) 
# 8 = max(7, 8, 7) 
# Do this in O(n) time and O(k) space. You can modify the input array in-place and you do not need to
# store the results. You can simply print them out as you compute them

def sub_max_array(array, k):
    if k > len(array):
        raise RuntimeError("k must be smaller than length of array!")
    for i in range(len(array) - k + 1):
        array[i] = max(array[i:i+k])
    return array[:-k + 1]

def main():
    array = [10, 5, 2, 7, 8, 7]
    print("Input:", array,"\nArray of sub-array's maximum:", sub_max_array(array, 3))

if __name__ == "__main__":
    main()