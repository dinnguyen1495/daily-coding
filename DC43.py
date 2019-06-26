# Implement a stack that has the following methods:
#    - push(val), which pushes an element onto the stack
#    - pop(), which pops off and returns the topmost element of the stack. If there are no elements
#       in the stack, then it should throw an error or return null.
#    - max(), which returns the maximum value in the stack currently. If there are no elements in the
#       stack, then it should throw an error or return null.
# Each method should run in constant time.

import random

class Stack:
    def __init__(self):
        self.stack_list, self.max_list = [], []

    def __str__(self):
        return str(self.stack_list)

    def get_stack_size(self):
        return len(self.stack_list)

    def push(self, val):
        self.stack_list.append(val)
        if len(self.max_list) == 0:
            self.max_list.append(val)
            return
        if self.max_list[-1] > val:
            self.max_list.append(self.max_list[-1])
            return
        self.max_list.append(val)
    
    def pop(self):
        if len(self.stack_list) == 0:
            return None
        self.max_list.pop()
        return self.stack_list.pop()
    
    def max(self):
        if len(self.stack_list) == 0:
            return None
        return self.max_list[-1]

def main():
    def make_test(N, M, min_value, max_value):
        stack = Stack()
        for i in range(N):
            stack.push(random.randint(min_value, max_value))
        print('Length of stack after pushing:', stack.get_stack_size())
        print('Current max value of stack:',stack.max())
        for i in range(N - M):
            stack.pop()
        print('Length of stack after popping:', stack.get_stack_size())
        print('Current max value of stack:',stack.max())
    make_test(10000, 100, -50000, 10000)

if __name__ == '__main__':
    main()