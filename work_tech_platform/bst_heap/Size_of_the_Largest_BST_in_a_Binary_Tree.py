"""
https://workat.tech/problem-solving/practice/size-of-largest-bst-in-binary-tree

https://www.techiedelight.com/find-size-largest-bst-in-binary-tree/
"""
import sys


# A class to store a BST node
class Node:
    # constructor
    def __init__(self, data, left=None, right=None):
        self.data = data
        self.left = left
        self.right = right


# Recursive function to calculate the size of a given binary tree
def size(root):
    # base case: empty tree has size 0
    if root is None:
        return 0

    # recursively calculate the size of the left and right subtrees and
    # return the sum of their sizes + 1 (for root node)
    return size(root.left) + 1 + size(root.right)


# Recursive function to determine if a given binary tree is a BST or not
# by keeping a valid range (starting from [-INFINITY, INFINITY]) and
# keep shrinking it down for each node as we go down recursively
def isBST(node, min, max):
    # base case
    if node is None:
        return True

    # if the node's value falls outside the valid range
    if node.data < min or node.data > max:
        return False

    # recursively check left and right subtrees with updated range
    return isBST(node.left, min, node.data) and isBST(node.right, node.data, max)


class Solution:
    # Recursive function to find the size of the largest BST in a given binary tree
    def findLargestBST(self, root):
        if isBST(root, -sys.maxsize, sys.maxsize):
            return size(root)

        return max(self.findLargestBST(root.left), self.findLargestBST(root.right))


if __name__ == '__main__':
    ''' Construct the following tree
              10
            /    \
           /      \
          15       8
         /  \     / \
        /    \   /   \
       12    20 5     2
    '''

    root = Node(10)

    root.left = Node(15)
    root.right = Node(8)

    root.left.left = Node(12)
    root.left.right = Node(20)

    root.right.left = Node(5)
    root.right.right = Node(2)
    solve = Solution()
    print('The size of the largest BST is', solve.findLargestBST(root))