# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        self.ans=[]
        def abc(node):
            if node is None:
                return []
            self.ans.append(node.val)
            abc(node.left)
            abc(node.right)
        abc(root)
        return self.ans
            
        