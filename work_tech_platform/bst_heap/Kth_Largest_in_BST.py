"""
https://workat.tech/problem-solving/practice/kth-largest-element-bst

https://www.geeksforgeeks.org/kth-largest-element-bst-using-constant-extra-space/

https://www.geeksforgeeks.org/kth-largest-element-in-bst-when-modification-to-bst-is-not-allowed/
"""
class newNode:
    def __init__(self, data):
        self.data = data
        self.right = self.left = None

class Solution:

    def findKthLargest(self, root, k):
        curr = root
        Klargest = None

        # count variable to keep count
        # of visited Nodes
        count = 0

        while curr is not None:

            # if right child is None
            if curr.right is None:

                # first increment count and
                # check if count = k
                count += 1
                if count == k:
                    Klargest = curr

                # otherwise move to the left child
                curr = curr.left

            else:

                # find inorder successor of
                # current Node
                succ = curr.right

                while succ.left is not None and succ.left != curr:
                    succ = succ.left

                if succ.left is None:

                    # set left child of successor
                    # to the current Node
                    succ.left = curr

                    # move current to its right
                    curr = curr.right

                # restoring the tree back to
                # original binary search tree
                # removing threaded links
                else:

                    succ.left = None
                    count += 1
                    if count == k:
                        Klargest = curr

                    # move current to its left child
                    curr = curr.left

        return Klargest.data


# Driver Code
if __name__ == '__main__':
    # Constructed binary tree is
    #     4
    #     / \
    # 2     7
    # / \ / \
    # 1 3 6 10
    root = newNode(4)
    root.left = newNode(2)
    root.right = newNode(7)
    root.left.left = newNode(1)
    root.left.right = newNode(3)
    root.right.left = newNode(6)
    root.right.right = newNode(10)
    solve = Solution()
    print("Finding K-th largest Node in BST : ",
          solve.findKthLargest(root, 2))