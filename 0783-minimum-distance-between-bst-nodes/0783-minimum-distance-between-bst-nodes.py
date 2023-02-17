# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minDiffInBST(self, root: Optional[TreeNode]) -> int:
        self.res=[]
        def dfs(node):
            if not node:
                return []
            dfs(node.left)
            self.res.append(node.val)
            dfs(node.right)
        dfs(root)
        print(self.res)
        m=float('inf')
        l=len(self.res)
        for i in range(l-1):
            m=min(m,self.res[i+1]-self.res[i])
        return m
            
            
        
    
        
        