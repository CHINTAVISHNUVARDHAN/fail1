class Node:
    def _init_(self, value):
        self.value = value
        self.left = None
        self.right = None

def print_level(root, level):
    if root is None:
        return
    if level == 1:
        print(root.value, end=' ')
    elif level > 1:
        print_level(root.left, level - 1)
        print_level(root.right, level - 1)

# Example usage:
# Create a sample tree
#       1
#      / \
#     2   3
#    / \   \
#   4   5   6

root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)
root.right.right = Node(6)

# Print nodes at level 3
print_level(root, 3)
# Output will be: 4 5 6
