# Daily Coding 6:
# An XOR linked list is a more memory efficient doubly linked list. 
# Instead of each node holding next and prev fields, it holds a field named both, 
# which is an XOR of the next node and the previous node. Implement an XOR linked list; 
# it has an add(element) which adds the element to the end, and a get(index) which returns the node at index.
# If using a language that has no pointerss (such as Python), you can assume you have access 
# to get_pointer and dereference_pointer functions that converts between nodes and memory addresses.

class Node:
    def __init__(self, value, next, prev):
        self.value = value
        if next and prev:
            print("Wrong input for a linked list!\n")
            return None
        if not prev: 
            self.both = next
        else: 
            self.both = prev

class LinkedList:
    def __init__(self, node):
        self.head = node

    def add(self, element):
        prev = None
        current = self.head
        if current is not None:
            self.head = Node(element, None, None)
            return
        next = current.both
        while prev != next:
            prev = current
            current = next
            next = current.both
        current.both = Node(element, None, current)

    def get(self, index):
        if self.head is None:
            print("Can't get element at index: ", index)
            return None
        if (index == 0):
            return self.head
        prev = None
        current = self.head
        next = current.both
        i = 0
        while prev != next:
            i += 1
            prev = current
            current = next
            next = current.both
            if i == index:
                return current
        print("Index out of bound: ", index)
        return None
    
    def list_of_values(self):
        if self.head is None: 
            return []
        prev = None
        current = self.head
        next = current.both
        list = [current.value]
        while prev != next:
            prev = current
            current = next
            next = current.both
            list.append(current.value)
        return list

def main():
    linked_list = LinkedList(None)
    linked_list.add(1)
    linked_list.add(3)
    linked_list.add(9)
    linked_list.add(2)
    linked_list.add(5)
    print("XOR Linked list at index 0:", linked_list.get(0).value)
    print("XOR Linked list at index 1:", linked_list.get(1).value)
    print("XOR Linked list at index 2:", linked_list.get(2).value)
    print("XOR Linked list at index 3:", linked_list.get(3).value)
    print("XOR Linked list at index 4:", linked_list.get(4).value)
    #print("XOR Linked list at index 5:", linked_list.get(5).value)  
    print("List of values:", linked_list.list_of_values())

if __name__ == "__main__":
    main()