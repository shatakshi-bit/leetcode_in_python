class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        
        par=[i for i in range(len(isConnected))]

        rank=[1]*(len(isConnected))

        def find(n):
            p=n
            while p!=par[p]:
                par[p]=par[par[p]]
                p=par[p]
            return p
        
        def union(n1,n2):
            p1,p2=find(n1),find(n2)
            if p1==p2:
                return 0

            if par[p1]>par[p2]:
                par[p2]=p1
                rank[p1]+=rank[p2]
            else:

                par[p1]=p2
                rank[p2]+=rank[p1]
            return 1

        count=len(isConnected)
        for i in range(len(isConnected)):
            for j in range(len(isConnected[i])):

                if isConnected[i][j]==1:
                    count-=union(i,j)
        return count
#         n=len(isConnected)
#         par=[i for i in range(n)]
#         rank=[1]*n
        
#         def find(n1):
#             res=n1
#             while res!=par[n1]:
#                 par[res]=par[par[n1]]
#                 res=par[n1]
#             return res
#         def union(n1,n2):
#             p1,p2=find(n1),find(n2)
#             if p1==p2:
#                 return 0
#             if rank[p2]>rank[p1]:
#                 par[p1]=p2
#                 rank[p2]+=rank[p1]
#             else:
#                 par[p2]=p1
#                 rank[p1]+=rank[p2]
#             return 1
#         ans=n
#         for i in range(n):
#             for j in range(len(isConnected[i])):
#                 if isConnected[i][j]==1:
#                     ans-=union(i,j)
#         return ans
                
                
                
            
        
    
            
            
            
            
        
        