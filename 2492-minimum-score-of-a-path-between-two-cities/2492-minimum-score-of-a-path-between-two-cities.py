class Solution:
    def minScore(self, n: int, roads: List[List[int]]) -> int:
        #TC-->O(E+V)
#         adj=defaultdict(list)
#         for src,dst,distance in roads:
#             adj[src].append((dst,dist))
#             adj[dst].append((src,dist))
        
#         def dfs(i):
#             if i in visited:
#                 return
#             visited.add(i)
#             for nei,dist in adj[i]:
#                 self.res=min(self.res,dist)
#                 dfs(nei)
#         self.res=float("inf")   
#         visited=set()
#         dfs(1)
#         return self.res
        
        h=defaultdict(list)
        for i,j,k in roads:
            h[i].append((j,k))
            h[j].append((i,k))
        def dfs(i):
            if i in visit:
                return
            visit.add(i)
            for nei,dist in h[i]:
                self.res=min(self.res,dist)
                dfs(nei)
        visit=set()
        self.res=float("inf")
        dfs(1)
        return self.res
            
            