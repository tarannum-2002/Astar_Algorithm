import math

def Astar(graph, start, end):
    def heuristic(node):
        return math.sqrt((node[0] - end[0])**2 + (node[1] - end[1])**2)

    boundary_nodes = {start}
    distances = {start: 0}
    g_values = {start: 0}
    came_from = {}

    while len(boundary_nodes) > 0:
        cur_node = min(boundary_nodes, key=lambda x: g_values[x] + heuristic(x))
        boundary_nodes.remove(cur_node)
        if cur_node == end:
            path = [end]
            while path[-1] != start:
                path.append(came_from[path[-1]])
            path.reverse()
            return path,g_values[end]
        
        for neighbor in graph[cur_node]:
            g = g_values[cur_node] + 1
            if neighbor not in g_values or g_values[neighbor] > g:
                g_values[neighbor] = g
                distances[neighbor] = distances[cur_node] + 1
                boundary_nodes.add(neighbor)
                came_from[neighbor] = cur_node
                
    return None




# Example graph represented as an adjacency list
graph = {
    (0, 0): [(0, 1), (1, 0)],
    (0, 1): [(0, 0), (1, 1)],
    (1, 0): [(0, 0), (1, 1)],
    (1, 1): [(0, 1), (1, 0)],
}

start = (0, 0)
end = (1, 1)

result, value = Astar(graph, start, end)
print(result)
print(value)
