class Solution:
    def maximumUnits(self, boxTypes: List[List[int]], truckSize: int) -> int:
#         d,l={},[]
#         ans=0
#         for i in range(len(boxTypes)):
#             v=boxTypes[i]
#             l.append(v[1])
#             d[v[1]]=v[0]
#         l=sorted(l,reverse=True)
#         print(d)
#         print(l)
#         for j in l:
#             if d[j]<truckSize and truckSize>0 :
#                 ans=ans+(j*d[j])
#                 truckSize-=d[j]
#             else:
#                 ans=ans+(truckSize*j)
#                 truckSize=0
#         return ans
                
        
                
                
        
                
            
        boxTypes.sort(key=lambda x:x[1],reverse=True)
        i = 0
        res = 0
        n = len(boxTypes)
        while truckSize>0 and i<n:
            if(truckSize > boxTypes[i][0]):
                res += boxTypes[i][0]*boxTypes[i][1]
                truckSize -= boxTypes[i][0]
            else:
                res += truckSize*boxTypes[i][1]
                truckSize=0
            i+=1
        return res

        
        