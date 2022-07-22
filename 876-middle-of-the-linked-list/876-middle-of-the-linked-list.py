# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        start=node=head
        length_list=0
        while start:
            length_list+=1
            start=start.next
        mid=length_list//2
        count=0
        while node:
            if count==mid:
                return node
            else:
                count+=1
                node=node.next
        

            
        
        