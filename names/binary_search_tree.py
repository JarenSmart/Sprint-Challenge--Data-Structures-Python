class BSTNode:
    def __init__(self, value):
        self.value = value
        self.left: BSTNode = None
        self.right: BSTNode = None

    # Insert the given value into the tree
    def insert(self, value):
        if value < self.value:
            if not self.left:
                self.left = BSTNode(value)
            else:
                self.left.insert(value)
        else:
            value >= self.value
            if not self.right:
                self.right = BSTNode(value)
            else:
                self.right.insert(value)

    # Return True if the tree contains the value
    # False if it does not
    def contains(self, target):
        # Contains:
        # Compare target value to node.value
        if target == self.value:
            return True
        else:
            if target >= self.value:
                # Go right
                if self.right is None:
                    # We've traversed the tree and haven't found it
                    return False
                else:
                    return self.right.contains(target)
            else:
                # Do same as above
                # Else if target < node.value
                if target <= self.value:
                    # Go left
                    # if node.left is None:
                    if self.left is None:
                        # return False
                        return False
                    else:
                        # return node.left.contains(target)
                        return self.left.contains(target)

    # Return the maximum value found in the tree

    def get_max(self):
        if not self.right:
            return self.value
        return self.right.get_max()

    # Call the function `fn` on the value of each node
    def for_each(self, fn):
        fn(self.value)
        if self.left:
            self.left.for_each(fn)
        if self.right:
            self.right.for_each(fn)
