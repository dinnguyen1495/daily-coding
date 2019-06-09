# Daily Coding 24
# Implement locking in a binary tree. A binary tree node can be locked or unlocked
# only if all of its descendants or ancestors are not locked.
# Design a binary tree node class with the following methods:
# - is_locked, which returns whether the node is locked
# - lock, which attempts to lock the node. If it cannot be locked, then it should
#   return false. Otherwise, it should lock it and return true.
# - unlock, which unlocks the node. If it cannot be unlocked, then it should return
#   false. Otherwise, it should unlock it and return true.
# You may augment the node to add parent pointers or any other property you would
# like. You may assume the class is used in a single-threaded program, so there is
# no need for actual locks or mutexes. Each method should run in O(h), where h is
# the height of the tree.

class LockedNode(object):
    def __init__(self, v, l = None, r = None, p = None):
        self.value = v
        self.locker = False
        self.left = l
        self.right = r
        self.parent = p
        self.locked_descendants = 0

    def is_locked(self):
        return self.locker

    def can_be_locked_or_unlocked(self):
        if self.locked_descendants > 0:
            return False
        current = self.parent
        while current:
            if current.is_locked:
                return False
            current = current.parent
        return True
    
    def lock(self):
        if self.can_be_locked_or_unlocked():
            self.locker = True
            current = self.parent
            while current:
                current.locked_descendants += 1
                current = current.parent
            return True
        return False

    def unlock(self):
        if self.can_be_locked_or_unlocked():
            self.locker = False
            current = self.parent
            while current:
                current.locked_descendants -= 1
                current = current.parent
            return True
        return False

def main():
    tree = LockedNode(1, None, None, None)
    print(tree.is_locked())
    print(tree.lock())
    print(tree.is_locked())
    print(tree.unlock())
    print(tree.is_locked())

if __name__ == "__main__":
    main()