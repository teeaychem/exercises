# Given the root of a binary tree, return the postorder traversal of its nodes' values.

# Example 1:


# Input: root = [1,null,2,3]
# Output: [3,2,1]
# Example 2:

# Input: root = []
# Output: []
# Example 3:

# Input: root = [1]
# Output: [1]

# Solution is the same as preorder traversal, but root.val added after l/r branches have been explored.

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        if root == None:
            return []
        else:
            collection = []
            if root.left != None:
                collection += Solution.postorderTraversal(self, root=root.left)
            if root.right != None:
                collection += Solution.postorderTraversal(self, root=root.right)
            collection += [root.val]

            return collection