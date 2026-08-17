"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if node is None:
            return node

        cache = dict() #points from original node to its copied node

        def clone_node(sub_node):

            if sub_node in cache:
                return cache[sub_node]
            

            new_node = Node(sub_node.val, [])
            cache[sub_node] = new_node
            for n in sub_node.neighbors:
                new_node.neighbors.append(clone_node(n))

            return new_node
        
        clone_node(node)
        return cache[node]
            

            



