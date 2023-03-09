# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def detectCycle(self, A: Optional[ListNode]) -> Optional[ListNode]:
        if not A or not A.next:
            return None
        slow,fast,entry=A,A,A
        while fast and fast.next:
            slow=slow.next
            fast=fast.next.next
            if slow==fast:
                while slow!=entry:
                    entry=entry.next
                    slow=slow.next
                return entry 
        return None
        