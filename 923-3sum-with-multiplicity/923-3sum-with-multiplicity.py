import collections
class Solution:
    def threeSumMulti(self, arr: List[int], target: int) -> int:
            count = [0 for i in range(0,101)]
            for i in arr:
                count[i]+=1
            result=0
            for i in range(0,101):
                 for j in range(i,101):
                        k = target-i-j
                        if k<0 or k>100:
                                continue
                        if i==j and j==k:
                                result+=(count[i]*(count[i]-1)*(count[i]-2))//6
                        elif i==j and j!=k:
                                result+= ((count[i] * (count[i]-1))//2)*count[k]
                        elif i<j and j<k:
                                result+= count[i]*count[j]*count[k]
            return result%(10**9+7)
                        

        
        # c=0
        # for i in range(len(arr)):
        #     for j in range(len(arr)):
        #         for k in range(len(arr)):
        #             if i<j and j<k and (arr[i]+arr[j]+arr[k])==target:
        #                 c=c+1
   
       