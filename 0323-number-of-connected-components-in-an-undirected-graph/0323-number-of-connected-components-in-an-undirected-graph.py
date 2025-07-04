class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        adj = {i: [] for i in range(n)}
        for u,v in edges:
            adj[u].append(v)
            adj[v].append(u)


        seen = set()

        def dfs(node):
            for i in adj[node]:
                if i not in seen:
                    seen.add(i)
                    dfs(i)

        count = 0
        for i in range(n):
            if i not in seen:
                seen.add(i)
                dfs(i)
                count += 1       

        return count    