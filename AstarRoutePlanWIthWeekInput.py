import heapq

def a_star(adj_list, start, goal, day):
    cost = 0
    heap = [(cost, start, [])]
    visited = set()
    
    while heap:
        cost, node, path = heapq.heappop(heap)
        
        if node == goal:
            return cost, path + [node]
        
        if node in visited:
            continue
        
        visited.add(node)
        neighbors = adj_list[node]
        
        for neighbor in neighbors:
            new_cost = cost + 1
            if day == "Saturday" or day == "Sunday":
                if node[0] == node[1]:
                    new_cost += 10
            heapq.heappush(heap, (new_cost, neighbor, path + [node]))
    
    return float("inf"), []

# adj_list = {
#     (0, 0): [(0, 1), (1, 0)],
#     (0, 1): [(0, 0), (0, 2), (1, 1)],
#     (0, 2): [(0, 1), (1, 2)],
#     (1, 0): [(0, 0), (1, 1)],
#     (1, 1): [(0, 1), (1, 0), (1, 2), (2, 1)],
#     (1, 2): [(0, 2), (1, 1), (2, 2)],
#     (2, 1): [(1, 1), (2, 2)],
#     (2, 2): [(1, 2), (2, 1)]
# }

graph = {
    (0, 0): [(0, 1), (1, 0)],
    (0, 1): [(0, 0), (1, 1),(0,2)],
    (0, 2): [(0,1), (1,2)],
    (1, 0): [(0, 0), (1, 1)],
    (1, 2): [(2, 2), (0, 2)],
    (1, 1): [(0, 1), (1, 0), (2,2)],
    (2, 0) : [(2,1)], 
    (2, 1): [ (2,0), (1,1)],
    (2,2): [(1,2), (1,1)]
}
start = (0, 0)
goal = (2, 2)
day = "Saturday"

cost, path = a_star(graph, start, goal, day)
print("Cost:", cost)
print("Path:", path)
