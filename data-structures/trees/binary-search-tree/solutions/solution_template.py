class Node:
    def __init__(self, val: int):
        self.val = val
        self.left = None
        self.right = None


class BinarySearchTree:
    """
    Template for BinarySearchTree implementation.
    Implement the methods below to maintain standard BST properties.
    """

    def __init__(self):
        self.root = None

    def insert(self, val: int) -> Node:
        """
        Inserts a new value into the BST and returns the new root.
        """
        pass

    def search(self, val: int) -> Node:
        """
        Searches for a value in the BST and returns the Node
        containing the value, or None if not found.
        """
        pass

    def delete(self, val: int) -> Node:
        """
        Deletes the given value from the BST and returns the new root.
        """
        pass
