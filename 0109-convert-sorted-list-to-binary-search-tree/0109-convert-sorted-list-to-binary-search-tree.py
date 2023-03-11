# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sortedListToBST(self, head: Optional[ListNode]) -> Optional[TreeNode]:
        a=[]
        while head:
            a.append(head.val)
            head=head.next
        def bst(a,l,r):
            if l>r:
                return None
            m=l+(r-l)//2
            root=TreeNode(a[m])
            root.left=bst(a,l,m-1)
            root.right=bst(a,m+1,r)
            return root
        return bst(a,0,len(a)-1)
       
            
       
        
       
          
            
            
        
            
            
            
        
#     def sortedListToBST1(self, head):
#         ls = []
#         while head:
#             ls.append(head.val)
#             head = head.next
#         return self.helper(ls, 0, len(ls)-1)

#     def helper(self, ls, start, end):
#         if start > end:
#             return None
#         if start == end:
#             return TreeNode(ls[start])
#         mid = (start+end) >> 1
#         root = TreeNode(ls[mid])
#         root.left = self.helper(ls, start, mid-1)
#         root.right = self.helper(ls, mid+1, end)
#         return root
