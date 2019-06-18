# Daily Coding 36
# Given the root to a binary search tree, find the second largest node in the tree.

class BSNode:
    def __init__(self, v):
        self.value = v
        self.left = None
        self.right = None
    
    def __str__(self):
        return '(' + str(self.value) + ' ' + (self.left.__str__() if self.left is not None else '_') + ' ' + \
            (self.right.__str__() if self.right is not None else '_') + ')'

    def add(self, value):
        if value < self.value:
            if self.left is None:
                self.left = BSNode(value)  
            else:
                self.left.add(value)
        if value > self.value:
            if self.right is None:
                self.right = BSNode(value)  
            else: 
                self.right.add(value)

    def largest_node(self):
        max_node = self
        while max_node.right is not None:
            max_node = max_node.right
        return max_node

    def second_largest_node(self):
        if self.left is None and self.right is None:
            return None
        if self.right is None:
            return self.left.largest_node()
        second_max = self
        max_right = self.right
        while max_right.right is not None:
            second_max = max_right
            max_right = max_right.right
        if max_right.left is not None:
            temp = max_right.left.largest_node()
            if temp.value > second_max.value:
                second_max = temp  
        return second_max.value

class BSTree:
    def __init__(self, node = None):
        self.root = node

    def __str__(self):
        return self.root.__str__()

    def add(self, value):
        self.root.add(value)    

    def second_largest_node(self):
        return self.root.second_largest_node()

def main():    
    tree = BSTree(BSNode(50)) 
    tree.add(30)
    tree.add(20)
    tree.add(40)
    tree.add(70)
    tree.add(60)
    tree.add(80)
    print("BSTree:", tree)
    print("Second largest node:", tree.second_largest_node())

if __name__ == '__main__':
    main()