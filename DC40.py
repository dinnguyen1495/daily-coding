# Daily Coding 40
# Given an array of integers where every integer occurs three times except for one integer, which
# only occurs once, find and return the non-duplicated integer.
# For example, given [6, 1, 3, 3, 3, 6, 6], return 1. Given [13, 19, 13, 13], return 19.
# Do this in O(N) time and O(1) space.

def non_duplicated_integer(array):
    dict = {}
    for number in array:
        if number not in dict:
            dict[number] = 1
        else:
            dict[number] += 1
            if dict[number] == 3:
                dict.pop(number)
    return list(dict.keys())[0]

def main():
    list_1 = [6, 1, 3, 3, 3, 6, 6]
    print('Non-duplicated integer of', list_1, 'is', non_duplicated_integer(list_1))
    list_2 = [13, 19, 13, 13]
    print('Non-duplicated integer of', list_2, 'is', non_duplicated_integer(list_2))
    
if __name__ == '__main__':
    main()