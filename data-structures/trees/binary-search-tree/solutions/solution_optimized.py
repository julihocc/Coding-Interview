class Node:
    def __init__(self, val: int):
        self.val = val
        self.left = None
        self.right = None


class BinarySearchTree:
    """
    Optimized solution for the BinarySearchTree.
    Time Complexity:
    - Insert: O(h)
    - Search: O(h)
    - Delete: O(h)
    where h is the height of the tree.
    """

    def __init__(self):
        self.root = None

    def insert(self, val: int) -> Node:
        self.root = self._insert_recursive(self.root, val)
        return self.root

    def _insert_recursive(self, root: Node, key: int) -> Node:
        if root is None:
            return Node(key)
        else:
            if root.val < key:
                root.right = self._insert_recursive(root.right, key)
            else:
                root.left = self._insert_recursive(root.left, key)
        return root

    def search(self, val: int) -> Node:
        return self._search_recursive(self.root, val)

    def _search_recursive(self, root: Node, key: int) -> Node:
        if root is None or root.val == key:
            return root
        if root.val < key:
            return self._search_recursive(root.right, key)
        return self._search_recursive(root.left, key)

    def delete(self, val: int) -> Node:
        self.root = self._delete_recursive(self.root, val)
        return self.root

    def _min_value_node(self, node: Node) -> Node:
        current = node
        while current.left is not None:
            current = current.left
        return current

    def _delete_recursive(self, root: Node, key: int) -> Node:
        if root is None:
            return root

        if key < root.val:
            root.left = self._delete_recursive(root.left, key)
        elif key > root.val:
            root.right = self._delete_recursive(root.right, key)
        else:
            # Node with only one child or no child
            if root.left is None:
                temp = root.right
                root = None
                return temp
            elif root.right is None:
                temp = root.left
                root = None
                return temp

            # Node with two children: Get the inorder successor
            temp = self._min_value_node(root.right)
            root.val = temp.val
            root.right = self._delete_recursive(root.right, temp.val)

        return root
