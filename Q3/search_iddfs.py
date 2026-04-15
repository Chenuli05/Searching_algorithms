from maze import get_neighbors, node_to_xy
import math

def iterative_deepening_dfs(current, goal, barriers, limit, path, visited_order, path_set):
    visited_order.append(current)

    if current == goal:
        return path + [current]
    if limit == 0:
        return None

    path_set.add(current)

    for neighbor in get_neighbors(current, barriers):
        if neighbor not in path_set:
            result = iterative_deepening_dfs(
                neighbor, goal, barriers, limit - 1, path +[current], visited_order, path_set
            )
            if result is not None:
                return result
    path_set.remove(current)
    return None

#cost of moving from one node to another
def edge_cost(node1, node2):
    x1, y1 = node_to_xy(node1)
    x2, y2 = node_to_xy(node2)

    dx = abs(x1 - x2)
    dy = abs(y1 - y2)

    if dx == 1 and dy == 1:
        return math.sqrt(2)   # diagonal
    elif dx + dy == 1:
        return 1              # horizontal or vertical
    #return None


def iddfs(start, goal, barriers, max_depth=36):
    all_visited =[]
    for depth in range(max_depth+ 1):
        visited_order = []
        path = iterative_deepening_dfs(
            current=start, goal=goal, barriers=barriers, limit=depth, path=[], visited_order=visited_order, path_set=set()
        )
        all_visited.extend(visited_order)


        if path is not None:
            return {
                "visited_order": all_visited,
                "time_taken": len(all_visited),
                "final path": path
            }
    return {
        "visited_order": all_visited,
        "time_taken": len(all_visited),
        "final path": None
    }



