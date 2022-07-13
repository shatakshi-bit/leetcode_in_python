# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
       #BFS solution
        
        if not root: return []
        
        ans = {}   #store the right-most value in each level
        queue = [(root, 0)]   #queue contains current vertex and level
        
        #Do the BFS
        while(queue):
            node, level = queue.pop(0)
            ans[level] = node.val       #for each level, right child will override the left child
            
            if node.left:
                queue.append((node.left, level + 1))
            if node.right:
                queue.append((node.right, level + 1))
            
        return ans.values()
    

           
           