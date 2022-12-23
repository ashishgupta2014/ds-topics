# Python3 program to check
# if a given tree is BST.
import math

# A binary tree node has data,
# pointer to left child and
# a pointer to right child
"""
https://workat.tech/problem-solving/practice/is-binary-tree-bst

https://www.geeksforgeeks.org/a-program-to-check-if-a-binary-tree-is-bst-or-not/

https://leetcode.com/problems/validate-binary-search-tree/
"""
class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

class Solution:

    def isValidBST(self, root) -> bool:
        queue = [[root, [-10**31-1,10**31+1]]]
        while queue:
            node, borders = queue.pop()
            if not borders[0] < node.data < borders[1]:
                return False
            if node.left:
                queue.append([node.left,[borders[0], node.data] ])
            if node.right:
                queue.append([node.right,[node.data, borders[1]] ])
        return True
    def isBSTUtil(self, root, prev):

        # traverse the tree in inorder fashion
        # and keep track of prev node
        if root is not None:
            if self.isBSTUtil(root.left, prev):
                return False

            # Allows only distinct valued nodes
            if prev is not None and root.data <= prev.data:
                return False

            prev = root
            return self.isBSTUtil(root.right, prev)

        return True


    def isBST(self, root):
        prev = None
        return self.isBSTUtil(root, prev)


# Driver Code
if __name__ == '__main__':
    solve = Solution()
    root = Node(3)
    root.left = Node(2)
    root.right = Node(5)
    root.right.left = Node(1)
    root.right.right = Node(4)

    # Function call
    if solve.isValidBST(root):
        print("Is BST")
    else:
        print("Not a BST")

# This code is contributed by Srathore
