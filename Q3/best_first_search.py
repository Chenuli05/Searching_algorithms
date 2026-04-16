import heapq #to make sure the noes with the smallest heuristic func come out 1st
from maze import get_neighbors, node_to_xy
import math

def chebyshev_distance(node, goal_node):
    x1, y1 = node_to_xy(node)
    x2, y2 = node_to_xy(goal_node)

    return max(abs(x1 - x2), abs(y1 - y2)) #given equation

def manhattan_distance(node, goal_node):
    x1, y1 = node_to_xy(node)
    x2, y2 = node_to_xy(goal_node)
    return abs(x1 - x2) + abs(y1 - y2)


def euclidean_distance(node, goal_node):
    x1, y1 = node_to_xy(node)
    x2, y2 = node_to_xy(goal_node)
    return math.sqrt((x1 - x2) ** 2 + (y1 - y2) ** 2)


def diagonal_distance(node, goal_node):
    x1, y1 = node_to_xy(node)
    x2, y2 = node_to_xy(goal_node)
    dx = abs(x1 - x2)
    dy = abs(y1 - y2)
    return max(dx, dy) + (math.sqrt(2) - 1) * min(dx, dy)

def best_first_search(start, goal, barriers,heuristic_function):
    visited_nodes = []
    visited_set = set()

    # priority queue items: (heuristic, node, path)
    frontier = []
    #change the heuristic function
    heapq.heappush(frontier, (heuristic_function(start, goal), start, [start]))

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
                    (heuristic_function(neighbor, goal), neighbor, path + [neighbor])
                )

    return {
        "visited_nodes": visited_nodes,
        "time_taken": len(visited_nodes),
        "final_path": None
    }