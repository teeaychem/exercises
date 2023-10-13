# Given the roots of two binary trees p and q, write a function to check if they are the same or not.

# Two binary trees are considered the same if they are structurally identical, and the nodes have the same value.

# Example 1:


# Input: p = [1,2,3], q = [1,2,3]
# Output: true
# Example 2:

# Input: p = [1,2], q = [1,null,2]
# Output: false
# Example 3:


# Input: p = [1,2,1], q = [1,1,2]
# Output: false

# Constraints:

# The number of nodes in both trees is in the range [0, 100].
# -104 <= Node.val <= 104

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# Traverse the two trees at the same time in the same way.
# There's not much to this, other than being careful about comparing p and q when None is an issue and then p.val and q.val when nodes are for sure present.

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        if p == q == None:
            return True
        elif p == None or q == None:
            return False
        elif p.val == q.val:
            return self.isSameTree(p=p.left, q=q.left) and self.isSameTree(p=p.right, q=q.right)
        else:
            return False