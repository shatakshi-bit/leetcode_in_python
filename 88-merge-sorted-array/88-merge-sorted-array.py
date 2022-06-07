class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        
        """
        print(nums1,nums2,m,n)
        j=0
        if m==1 and n==0:
            return nums1
        elif m==0 and n==1:
            nums1[0]=nums2[0]
            return nums1
        else:    
            for i in range(m,len(nums1)):
                    nums1[i]=nums2[j]
                    j=j+1
            return nums1.sort()
