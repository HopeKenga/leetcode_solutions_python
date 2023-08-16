class Node:
    def __init__(self, val=None, neighbors=None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []

def clonedGraph(node):
    if not node:
        return None
    
    dicOfVisited = {}
    
    def dfs(original):
        if original in dicOfVisited:
            return dicOfVisited[original]
        
        clonedNode = Node(original.val)
        dicOfVisited[original] = clonedNode
        
        for neighbor in original.neighbors:
            clonedNeighbor = dfs(neighbor)  # Use dfs to clone neighbors
            clonedNode.neighbors.append(clonedNeighbor)
        
        return clonedNode
    
    return dfs(node)

node1 = Node(1)
node2 = Node(2)
node1.neighbors.append(node2)
node2.neighbors.append(node1)

cloned_node1 = clonedGraph(node1)
