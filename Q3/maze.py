import random

grid_size = 6
total_nodes = grid_size * grid_size

def node_to_xy(node):
    x = node % grid_size
    y = node // grid_size

    return (x, y)

def xy_to_node(x, y):
    return y * grid_size + x

def generate_maze():
    # start node from 0 to 11
    start = random.randint(0, 11)

    # goal node from 24 to 35
    goal = random.randint(24, 35)

    # remaining nodes excluding start and goal
    remaining_nodes = [n for n in range(total_nodes) if n not in (start, goal)]

    # choose 4 random barriers
    barriers = random.sample(remaining_nodes, 4)

    maze = {
        "start": start,
        "goal": goal,
        "barriers": barriers
    }

    return maze

# example run
maze = generate_maze()

print("Start node:", maze["start"], "Coordinates:", node_to_xy(maze["start"]))
print("Goal node:", maze["goal"], "Coordinates:", node_to_xy(maze["goal"]))
print("Barrier nodes:", maze["barriers"])
print("Barrier coordinates:", [node_to_xy(node) for node in maze["barriers"]])

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

print_maze(maze)