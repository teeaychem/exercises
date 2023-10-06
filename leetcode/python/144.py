# Given the root of a binary tree, return the preorder traversal of its nodes' values.

# Example 1:


# Input: root = [1,null,2,3]
# Output: [1,2,3]
# Example 2:

# Input: root = []
# Output: []
# Example 3:

# Input: root = [1]
# Output: [1]

# Main thing here was learning what preorder traversal means.
# In short: node -> left -> right
# That, and remembering the func is relative to a class and the syntax for named args.

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        if root == None:
            return []
        else:
            collection = [root.val]
            if root.left != None:
                collection += Solution.preorderTraversal(self, root=root.left)
            if root.right != None:
                collection += Solution.preorderTraversal(self, root=root.right)
            
            return collection