# Daily Coding 1
# This problem was recently asked by Google.
# Given a list of numbers and a number k, 
# return whether any two numbers from the list add up to k.

def is_add_up_to(arr, k):
    passed_elems = set()
    for i in range(len(arr)):
        if k - arr[i] in passed_elems:
            return True
        else:
            passed_elems.add(arr[i])
    return False

def main():
    test = [10, 15, 3, 7]
    print("Result for input {0} and {1}: {2}".format(test, 25, is_add_up_to(test, 25)))

if __name__ == "__main__":
    main()