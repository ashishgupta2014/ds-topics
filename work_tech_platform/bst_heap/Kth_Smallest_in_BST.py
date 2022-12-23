# A simple inorder traversal based Python3
# program to find k-th smallest element
# in a BST.

# A BST node


class Node:

    def __init__(self, key):

        self.data = key
        self.left = None
        self.right = None

# Recursive function to insert an key into BST


def insert(root, x):

    if root is None:
        return Node(x)
    if x < root.data:
        root.left = insert(root.left, x)
    elif x > root.data:
        root.right = insert(root.right, x)
    return root

# Function to find k'th largest element
# in BST. Here count denotes the number
# of nodes processed so far
"""
https://workat.tech/problem-solving/practice/kth-smallest-element-bst

https://www.geeksforgeeks.org/find-k-th-smallest-element-in-bst-order-statistics-in-bst/
"""
class Solution:
    k = None
    def kthSmallest(self, root):
        # Base case
        if root is None:
            return None

        # Search in left subtree
        left = self.kthSmallest(root.left)

        # If k'th smallest is found in
        # left subtree, return it
        if left is not None:
            return left

        # If current element is k'th
        # smallest, return it
        self.k -= 1
        if self.k == 0:
            return root

        # Else search in right subtree
        return self.kthSmallest(root.right)

    # Function to find k'th largest element in BST


    def printKthSmallest(self, root, k):
        self.k = k
        res = self.kthSmallest(root)

        if res is None:
            print("There are less than k nodes in the BST")
        else:
            print("K-th Smallest Element is ", res.data)


# Driver code
if __name__ == '__main__':

    root = None
    keys = [20, 8, 22, 4, 12, 10, 14]

    for x in keys:
        root = insert(root, x)

    k = 3
    solve = Solution()
    solve.printKthSmallest(root, k)

# This code is contributed by mohit kumar 29
