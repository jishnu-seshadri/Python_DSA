''' 
Depth first search

using visited nodes array and atack (LIFO array)
'''


def dfs(graph, node, visited = []):

    visited.append(node)
        #curr_node = stack.pop()
    for neighbour in graph[node]:
        if neighbour not in visited:
            dfs(graph, neighbour, visited)
                 
    return visited

visited = []
graph = {
  'A' : ['B','C'],
  'B' : ['D', 'E'],
  'C' : ['F'],
  'D' : [],
  'E' : ['F'],
  'F' : []
}

print(dfs(graph, 'A'))