# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        q = collections.deque([root])
        ans = []
        
        while q:
            
            #varaible changes to the rightMost Node
            rightMost = None
            
            #Traversing a level | i.e traversing till the end of the current len(q)
            for i in range(len(q)):
                node = q.popleft()
                
                if node:
                    
                    #Updating the rightMost node each time till we reach rightMost Node of the level
                    rightMost = node
                    q.append(node.left)
                    q.append(node.right)
                    
            #if rightMost is not null then append it to the ans
            if rightMost:
                ans.append(rightMost.val)
        
        return ans

           
           