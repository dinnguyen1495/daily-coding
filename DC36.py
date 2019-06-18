# Daily Coding 36
# Given the root to a binary search tree, find the second largest node in the tree.

class BSTree:
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
                self.left = BSTree(value)  
            else:
                self.left.add(value)
        if value > self.value:
            if self.right is None:
                self.right = BSTree(value) 
            else: 
                self.right.add(value)

    def largest_node_and_parent(self):
        max_node, parent = self, None
        while max_node.right is not None:
            parent = max_node
            max_node = max_node.right
        return max_node, parent

    def second_largest_node(self):
        if self.left is None and self.right is None:
            return None
        if self.right is None:
            result, _ = self.left.largest_node_and_parent()
            return result
        max_node, result = self.right.largest_node_and_parent()
        if max_node.left is not None:
            temp, _ = max_node.left.largest_node_and_parent()
            if temp.value > result.value:
                result = temp
        return result.value

def main():    
    tree = BSTree(50)
    tree.add(30)
    tree.add(20)
    tree.add(40)
    tree.add(70)
    tree.add(60)
    tree.add(80)
    tree.add(75)
    print("Test BSTree:", tree)
    print("Second largest node:", tree.second_largest_node())

if __name__ == '__main__':
    main()