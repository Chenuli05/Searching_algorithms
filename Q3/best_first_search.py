import heapq #to make sure the noes with the smallest heuristic func come out 1st
from maze import get_neighbors
from search_iddfs import chebyshev_distance

def best_first_search(start, goal, barriers):
    visited_nodes = []
    visited_set = set()

    # priority queue items: (heuristic, node, path)
    frontier = []
    heapq.heappush(frontier, (chebyshev_distance(start, goal), start, [start]))

    while frontier:
        h, current, path = heapq.heappop(frontier)

        if current in visited_set:
            continue

        visited_set.add(current)
        visited_nodes.append(current)

        if current == goal:
            return {
                "visited_nodes": visited_nodes,
                "time_taken": len(visited_nodes),
                "final_path": path
            }

        for neighbor in get_neighbors(current, barriers):
            if neighbor not in visited_set:
                heapq.heappush(
                    frontier,
                    (chebyshev_distance(neighbor, goal), neighbor, path + [neighbor])
                )

    return {
        "visited_nodes": visited_nodes,
        "time_taken": len(visited_nodes),
        "final_path": None
    }