# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def deepestLeavesSum(self, root: Optional[TreeNode]) -> int:
        max_level=float('-inf')
        sum=0
        def _helper(root,level):
            nonlocal max_level,sum
            if root:
                if level>max_level:
                    max_level=level
                    sum=root.val
                elif level==max_level:
                    sum+=root.val
                _helper(root.left,level+1)
                _helper(root.right,level+1)
        _helper(root,0)
        return sum
        