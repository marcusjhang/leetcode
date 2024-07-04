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
        if not node:
            return None

        queue = [node]
        orToNew = {}
        orToNew[node] = Node(val = node.val)

        while queue:
            currNode = queue.pop(0)

            for neighbor in currNode.neighbors:
                if neighbor not in orToNew:
                    orToNew[neighbor] = Node(val=neighbor.val)
                    queue.append(neighbor)
                orToNew[currNode].neighbors.append(orToNew[neighbor])

        return orToNew[node]
                