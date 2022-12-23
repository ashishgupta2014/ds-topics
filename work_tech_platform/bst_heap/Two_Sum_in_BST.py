# Python3 code to find a pair with given sum
# in a Balanced BST
"""
https://workat.tech/problem-solving/practice/two-sum-binary-search-tree

https://www.geeksforgeeks.org/find-a-pair-with-given-sum-in-bst/
"""

class Node:

    # Construct to create a new Node
    def __init__(self, key):
        self.data = key
        self.left = self.right = None


# A utility function to insert a new
# Node with given key in BST
class Solution:
    # def insert(self, root: Node, key: int):
    #     # If the tree is empty, return a new Node
    #     if root is None:
    #         return Node(key)
    #
    #     # Otherwise, recur down the tree
    #     if root.data > key:
    #         root.left = self.insert(root.left, key)
    #
    #     elif root.data < key:
    #         root.right = self.insert(root.right, key)
    #
    #     # return the (unchanged) Node pointer
    #     return root


    # Function that adds values of given BST into
    # ArrayList and hence returns the ArrayList
    def tree_to_list(self, root: Node, arr: list):
        if not root:
            return arr

        self.tree_to_list(root.left, arr)
        arr.append(root.data)
        self.tree_to_list(root.right, arr)

        return arr


    # Function that checks if there is a pair present
    def pairExists(self, root: Node, target: int) -> bool:
        # This list a1 is passed as an argument
        # in treeToList method which is later
        # on filled by the values of BST
        arr1 = []

        # a2 list contains all the values of BST
        # returned by treeToList method
        arr2 = self.tree_to_list(root, arr1)

        # Starting index of a2
        start = 0

        # Ending index of a2
        end = len(arr2) - 1

        while start < end:

            # If target found
            if arr2[start] + arr2[end] == target:
                print(f"Pair Found: {arr2[start]} + {arr2[end]} = {target}")
                return True

            # Decrements end
            if arr2[start] + arr2[end] > target:
                end -= 1

            # Increments start
            if arr2[start] + arr2[end] < target:
                start += 1

        print("No such values are found!")
        return False


# Driver code
if __name__ == "__main__":
    solve = Solution()
    root = None
    root = solve.insert(root, 15)
    root = solve.insert(root, 10)
    root = solve.insert(root, 20)
    root = solve.insert(root, 8)
    root = solve.insert(root, 12)
    root = solve.insert(root, 16)
    root = solve.insert(root, 25)

    solve.pairExists(root, 33)

