# Daily Coding 8:
# This problem was asked by Google.
# A unival tree (which stands for "universal value") is a tree where all nodes under it have the # same value.
# Given the root to a binary tree, count the number of unival subtrees.
# For example, the following tree has 5 unival subtrees:
#    0
#   / \
#  1   0
#     / \
#    1   0
#   / \
#  1   1

class Node:
    def __init__(self, value = None, left = None, right = None):
        self.value = value
        self.left = left
        self.right = right

    def isLeaf(self):
        return not self.left and not self.right

    def isEqual(self, node):
        if self.value == node.value:
            if self.isLeaf() and node.isLeaf():
                return True
            else:
                return isEqual(self.left, node.left) and isEqual(self.right, node.right)
    
    def isUnivalTree(self):
        return self.isLeaf() or self.left.isEqual(self.right)

    def unival_subtrees(self):
        if self.value is None:
            return 0
        counter = 0
        if self.isUnivalTree():
            counter += 1
        if self.left:
            counter += self.left.unival_subtrees()
        if self.right:
            counter += self.right.unival_subtrees()
        return counter 
    
class Tree:
    def __init__(self, node):
        self.root = node

    def unival_subtrees(self):
        return self.root.unival_subtrees()

def main():
    root = Node(0, Node(1, None, None), Node(0, Node(1, Node(1, None, None), Node(1, None, None)), Node(0, None, None)))
    tree = Tree(root)
    print("Number of unival subtrees: %i" %(tree.unival_subtrees()))

if __name__ == "__main__":
    main()