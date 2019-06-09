# Daily Coding 26
# Given a singly linked list and an integer k, remove the kth last element from the list. k is guaranteed
# to be smaller than the length of the list.
# The list is very long, so making more than one pass is prohibitively expensive.
# Do this in constant space and in one pass.

class Node:
    def __init__(self, value = None, next = None):
        self.value = value
        self.next = next
        
    def add(self, value):
        current = self
        while current.next:
            current = current.next
        current.next = Node(value, None)

    def __str__(self):
        result = ''
        current = self
        while current:
            result += str(current.value) + (' -> ' if current.next else '')
            current = current.next
        return result
    
    def remove(self, k):
        node = last_k = self
        for _ in range(k):
            node = node.next
        while node.next:
            last_k = last_k.next
            node = node.next
        last_k.next = last_k.next.next
        return self

def main():
    list = Node(None, None)
    for i in range(10000):
        list.add(i)
    list.remove(10)
    print(list)

if __name__ == "__main__":
    main()