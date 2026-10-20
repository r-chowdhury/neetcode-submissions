# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        res = [False]
        def dfs(root, currentSum):
            if root is None:
                return
            currentSum += root.val
            if root.left is None and root.right is None:
                if currentSum == targetSum:
                    res[0] = True
                return
            dfs(root.left, currentSum)
            dfs(root.right, currentSum)
            return
        dfs(root, 0)
        return res[0]