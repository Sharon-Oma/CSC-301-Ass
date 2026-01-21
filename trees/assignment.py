# Define a node of the Binary Search Tree
class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


#Function to insert a value into the BST
def insert(root, value):
    if root is None:
        return Node(value)

    if value < root.data:
        root.left = insert(root.left, value)
    else:
        root.right = insert(root.right, value)

    return root


# Inorder traversal (Left -> Root -> Right)
def inorder(root):
    if root:
        inorder(root.left)
        print(root.data, end=" ")
        inorder(root.right)


# Preorder traversal (Root -> Left -> Right)
def preorder(root):
    if root:
        print(root.data, end=" ")
        preorder(root.left)
        preorder(root.right)


# Postorder traversal (Left -> Right -> Root)
def postorder(root):
    if root:
        postorder(root.left)
        postorder(root.right)
        print(root.data, end=" ")


# Function to calculate height of the tree (in terms of edges)
def height(root):
    if root is None:
        return -1
    return 1 + max(height(root.left), height(root.right))


# Main program
values = [23, 5, 15, 8, 17, 10]
root = None

for value in values:
    root = insert(root, value)

print("Inorder Traversal:")
inorder(root)

print("\nPreorder Traversal:")
preorder(root)

print("\nPostorder Traversal:")
postorder(root)

print("\nHeight of the tree:", height(root))
