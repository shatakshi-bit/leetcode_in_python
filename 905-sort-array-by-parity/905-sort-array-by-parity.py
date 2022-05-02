class Solution:
    def sortArrayByParity(self, nums: List[int]) -> List[int]:
        a=[]
        if len(nums)>0:
            for i  in nums:
                if i%2==0:
                    a.append(i)
            for j in nums:
                if j%2!=0:
                    a.append(j)
            return a
        else:
            return nums


