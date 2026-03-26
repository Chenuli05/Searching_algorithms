import random

grid_size = 6
total_nodes = grid_size * grid_size

def node_to_xy(node):
    x = node // grid_size
    y = node % grid_size

    return x, y

def xy_to_node(x, y):
    return x * grid_size + y

def generate_maze():
    # start node from 0 to 11
    start = random.randint(0, 11)

    # goal node from 24 to 35
    goal = random.randint(24, 35)

    # remaining nodes excluding start and goal
    remaining_nodes = [n for n in range(total_nodes) if n not in (start, goal)]

    # choose 4 random barriers
    barriers = random.sample(remaining_nodes, 4)

    return {
        "start": start,
        "goal": goal,
        "barriers": barriers
    }

def get_neighbors(node, barriers):
    x, y = node_to_xy(node)

    directions = [
        (-1, 0), (1,0),
        (0,-1), (0,1),
        (-1,-1), (-1,1),
        (1, -1), (1,1)
    ]
    neighbors = []

    for dx, dy in directions:
        nx, ny= x+dx, y+dy
        if 0 <= nx < grid_size and 0 <= ny < grid_size:
            nxt = xy_to_node(nx, ny)
            if nxt not in barriers:
                neighbors.append(nxt)
    return sorted(neighbors)

# example run
# maze = generate_maze()
#


def print_maze(maze):
    for y in range(grid_size):
        row = []
        for x in range(grid_size):
            node = xy_to_node(x, y)

            if node == maze["start"]:
                row.append("S")
            elif node == maze["goal"]:
                row.append("G")
            elif node in maze["barriers"]:
                row.append("X")
            else:
                row.append(str(node))
        print("\t".join(row))

