# Daily Coding 35
# Given an array of strictly the characters 'R', 'G', and 'B', segregate the values of the array so
# that all the Rs come first, the Gs come second, and the Bs come last. You can only swap elements
# of the array.
# Do this in linear time and in-place.
# For example, given the array ['G', 'B', 'R', 'R', 'B', 'R', 'G'], it should become ['R', 'R', 'R',
# 'G', 'G', 'B', 'B'].

def rgb_sort(array):
    def swap(a, b):
        array[a], array[b] = array[b], array[a]

    left, right = 0, len(array) - 1
    while array[left] == 'R':
        left += 1
    while array[right] == 'B':
        right -= 1
    
    for i in range(left + 1, right + 1):
        if array[i] == 'R':
            swap(i, left)
            left += 1

    for j in range(right - 1, left - 1, -1):
        if array[j] == 'B':
            swap(j, right)
            right -= 1
    return array

def main():
    print(rgb_sort(['G', 'B', 'R', 'R', 'B', 'R', 'G']))
    print(rgb_sort(['B', 'B', 'G', 'G', 'G', 'R', 'R']))
    print(rgb_sort(['R', 'G', 'B', 'R', 'G', 'B', 'R']))

if __name__ == '__main__':
    main()