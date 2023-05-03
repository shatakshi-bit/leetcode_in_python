class Solution:
    def findDifference(self, nums1: List[int], nums2: List[int]) -> List[List[int]]:
        nums1=set(nums1)
        nums2=set(nums2)
        x,y=[],[]
        a=[]
        for i in nums1:
            if not i in nums2:
                x.append(i)
        for i in nums2:
            if i not in nums1:
                y.append(i)
        a.append(x)
        a.append(y)
        return a
        
        

        
                
                
        
        