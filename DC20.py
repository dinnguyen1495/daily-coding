# Daily Coding 20
# Given two singly linked lists that intersect at some point, find the intersecting node. The lists are
# non-cyclical.
# For example, given A = 3 -> 7 -> 8 -> 10 and B = 99 -> 1 -> 8 -> 10, return the node with value 8.
# In this example, assume nodes with the same value are the exact same node objects.
# Do this in O(M + N) time (where M and N are the lengths of the lists) and constant space.

class Node:
    def __init__(self, v, n):
        self.value = v
        self.next = n
    
    def to_string(self):
        if self.value is None:
            return ""
        result = ""
        node = self
        while node is not None:
            result += str(node.value) + (" -> " if node.next is not None else "")
            node = node.next
        return result

def get_length(list):
    length = 0
    node = list
    while node is not None:
        length += 1
        node = node.next
    return length

def find_intersect_part(list1, list2):
    d1, d2 = get_length(list1), get_length(list2)
    if d1 >= d2:
        loop_list, other_list = list1, list2
    else:
        loop_list, other_list = list2, list1
    dist = abs(d1 - d2)
    d = 0
    while d < dist and loop_list is not None:
        d += 1
        loop_list = loop_list.next
    while loop_list is not None and other_list is not None:
        if loop_list.value == other_list.value:
            return loop_list.value
        loop_list = loop_list.next
        other_list = other_list.next
    return None

def main():
    list1 = Node(5, Node(3, Node(7, Node(8, Node(10, None)))))
    print("List 1: " + list1.to_string())
    list2 = Node(99, Node(1, Node(8, Node(10, None))))
    print("List 2: " + list2.to_string())
    print("Intersection Node:", find_intersect_part(list1, list2))

if __name__ == "__main__":
    main()