class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        provinces = 0
        visited = set()
    
        def dfs(node: int):
            if node in visited:
                return
            visited.add(node)
            for j, val in enumerate(isConnected[node]):
                if val == 1 and node != j:
                    dfs(j)

        for i, _ in enumerate(isConnected):
            if i not in visited:
                dfs(i)
                provinces += 1
        return provinces
        