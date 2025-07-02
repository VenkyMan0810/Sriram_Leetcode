"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

from typing import Optional
class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if node is None:
            return None

        clone = {}

        def dfs(curr):
            if curr in clone:
                return clone[curr]
            
            copy = Node(curr.val)
            clone[curr] = copy

            for i in curr.neighbors:
                copy.neighbors.append(dfs(i))

            return copy

        return dfs(node)