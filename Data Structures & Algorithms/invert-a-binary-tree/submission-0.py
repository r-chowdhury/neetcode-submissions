# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if not root:
            return None
        queue = [root]
        while queue:
            cn = queue.pop(0)
            cn.left, cn.right = cn.right, cn.left
            if cn.left:
                queue.append(cn.left)
            if cn.right:
                queue.append(cn.right)
        return root
        