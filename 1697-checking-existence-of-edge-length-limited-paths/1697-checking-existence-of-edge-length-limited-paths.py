class Solution:
    def distanceLimitedPathsExist(self, n: int, edgeList: List[List[int]], queries: List[List[int]]) -> List[bool]:
        def find(n):
            while group[n] != n:
                n = group[n]
            return group[n]
        
        def union(n1, n2):
            p1, p2 = find(n1), find(n2)
            if p1 == p2:
                return
            if rank[p1] > rank[p2]:
                rank[p1] += 1
                group[p2] = p1
            else:
                rank[p2] += 1
                group[p1] = p2

        group = [i for i in range(n)]
        rank = [0] * n
        ans = [False] * len(queries)
        idx = 0
        
        for i in range(len(queries)):
            queries[i].append(i)

        edgeList.sort(key=lambda x: x[2])
        queries.sort(key=lambda x: x[2])

        for p, q, d, i in queries:
            while idx < len(edgeList) and edgeList[idx][2] < d:
                union(edgeList[idx][0], edgeList[idx][1])
                idx += 1
            ans[i] = find(p) == find(q)
        return ans
         
        