''' 
Breadth first search

using visited nodes array and queue (FIFO)
'''

# graph - adjacency list

def bfs(graph, s_node):
    visited = []
    queue = []
    visited.append(s_node)
    queue.append(s_node)

    while queue:
        curr_node = queue.pop(0)
        for neighbour in graph[curr_node]:
            if neighbour not in visited:
                visited.append(neighbour)
                queue.append(neighbour)
    
    return visited


graph = {
  'A' : ['B','C'],
  'B' : ['D', 'E'],
  'C' : ['F'],
  'D' : [],
  'E' : ['F'],
  'F' : []
}

print(bfs(graph, 'A'))