class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

    def add_Node(self, data):
        if self.data is None:
            self.data = data
        else:
            if data > self.data:
                if self.right:
                    self.right.add_Node(data)
                else:
                    self.right = Node(data)
            else:
                if self.left:
                    self.left.add_Node(data)
                else:
                    self.left = Node(data)


def display(root):
    """Preorder traversal"""
    if root is None:
        return
    print(root.data)
    display(root.left)
    display(root.right)


def find_sibling(root, x):
    """Find sibling of node with value x in BST"""
    if root is None:
        return None

    # Check if current node is parent of x
    if root.left and root.left.data == x:
        return root.right.data if root.right else None
    if root.right and root.right.data == x:
        return root.left.data if root.left else None

    # Search in left or right subtree
    if x < root.data:
        return find_sibling(root.left, x)
    else:
        return find_sibling(root.right, x)


def sibling(n, x, array):
    # Build BST
    root = Node(array[0])
    for ele in array[1:]:
        root.add_Node(ele)

    print("BST Preorder Traversal:")
    display(root)

    sib = find_sibling(root, x)
    if sib is not None:
        print(f"Sibling of {x} is: {sib}")
    else:
        print(f"{x} has no sibling.")
    return sib


if __name__ == "__main__":
    n = 5
    array = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24]
    x = 14
    res = sibling(n, x, array)
    print("Returned value:", res)
