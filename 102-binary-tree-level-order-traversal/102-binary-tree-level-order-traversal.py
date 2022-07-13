# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:return []
        ans,Q=[],[root]
        while Q:
            ans.append([n.val for n in Q])
            Q=[x for n in Q  for x in [n.left,n.right] if x]
        return ans
        