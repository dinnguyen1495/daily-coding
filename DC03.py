# Daily Coding 3
# Given the root to a binary tree, 
# implement serialize(root), which serializes the tree into a string, 
# and deserialize(s), which deserializes the string back into the tree.
# Time: 6h30'

class Node:
    def __init__(self, value = None, left = None, right = None):
        self.value = value
        self.left = left
        self.right = right

def serialize(tree):
    serial = ""
    serial += str(tree.value) + " " + (serialize(tree.left) if tree.left else "(None)") + " " +(serialize(tree.right) if tree.right else "(None)")
    return serial

def deserialize(string):
    list = string.split(" ")

    def helper(index):
        if list[index] == "(None)":
            return None, index + 1
        value = list[index]
        left, index = helper(index + 1)
        right, index = helper(index)
        return Node(value, left, right), index
    
    return helper(0)[0]

def main():
    tree = Node("root", Node("left", Node("left.left", None, None), None), Node("right", None, None))
    print(serialize(tree))
    print(serialize(deserialize(serialize(tree))))
      
if __name__ == "__main__":
    main()