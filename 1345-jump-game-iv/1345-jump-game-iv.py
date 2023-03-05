class Solution:
    def minJumps(self, arr: List[int]) -> int:
        E = len(arr) - 1
        if not E:
            return 0
        C = {}
        for i,x in enumerate(arr):
            if x in C:
                C[x].append(i)
            else:
                C[x] = [i]
        def getConns(n):
            a = arr[n]
            if a in C:
                for n2 in C[a]:
                    yield n2
                del C[a]
            if n>1:
                yield n-1
            if n<E:
                yield n+1
        d = {0:0}
        q = collections.deque([0])
        while True:
            if E in d:
                return d[E] # Success
            n = q.popleft()
            x = d[n] 
            for n2 in getConns(n):
                if n2 in d:
                    continue   # Point Already Visited
                d[n2] = x+1    # Lowest Distance for this Point
                q.append(n2)
        
            
#         n=len(arr)
        
#         d=defaultdict(list)
        
#         if n==1:
#             return 0
        
#         for i in range(n):
#             if arr[i] in arr:
#                 d[arr[i]].append(i)
                
        
#         visited=[False]*n
#         visited[0]=True
#         q=deque()
#         q.append(0)
#         steps=0
        
#         while q:
#             l=len(q)
#             while l>0:
#                 i=q.popleft()
#                 l-=1
                
#                 if i==(n-1):
#                     return steps
                  
#                 nxt=d[arr[i]]
#                 nxt.append(i-1)
#                 nxt.append(i+1)
                  
#                 for j in nxt:
#                     if j>=0 and j<n and not visited[j]:
#                         q.append(j)
#                         visited[j]=True
#                 nxt=[]
#             steps+=1
            
#         return -1
        