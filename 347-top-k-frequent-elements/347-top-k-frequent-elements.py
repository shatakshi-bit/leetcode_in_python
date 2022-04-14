class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        l={}
        for i in range(len(nums)):
            if nums[i] in l:
                l[nums[i]]+=1
            else:
                l[nums[i]]=1
        print(l)
        x=[]
        for i in l.values():
            x.append(i)
        x.sort(reverse=True)
        ans=[]
        i=0
        ll=dict(sorted(l.items(),key=operator.itemgetter(1),reverse=True))
        for n,v in ll.items():
            if k==0:
                break
            if x[i]==v:
                ans.append(n)
            k-=1
            i+=1
        return ans