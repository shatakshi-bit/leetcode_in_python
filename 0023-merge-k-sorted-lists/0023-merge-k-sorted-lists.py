# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        def merge_list(x,y):
            dummy=ListNode()
            tail=dummy  
            while x and y:
                if x.val < y.val:
                    tail.next=x
                    x=x.next
                else:
                    tail.next=y
                    y=y.next
                tail=tail.next
            if x:
                tail.next=x
            if y:
                tail.next=y
            return dummy.next
        if not lists or len(lists)==0:
            return None
        while len(lists)>1:
            combined_lists=[]
            for i in range(0,len(lists),2):
                list1=lists[i]
                list2=lists[i+1] if (i+1) <len(lists) else None
                combined_lists.append(merge_list(list1,list2))
            lists=combined_lists
        return lists[0]


       
