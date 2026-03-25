from maze import *
from search_iddfs import iddfs, edge_cost

maze = generate_maze()

print("Start node:", maze["start"])
print("Goal node:", maze["goal"])
print("Barrier nodes:", maze["barriers"])
print("Start node:", maze["start"], "Coordinates:", node_to_xy(maze["start"]))
print("Goal node:", maze["goal"], "Coordinates:", node_to_xy(maze["goal"]))
print("Barrier nodes:", maze["barriers"])
print("Barrier coordinates:", [node_to_xy(node) for node in maze["barriers"]])
print("Neighbors of start:", get_neighbors(maze["start"], set(maze["barriers"])))
print()
print_maze(maze)
print()

result = iddfs(
    start=maze["start"],
    goal=maze["goal"],
    barriers=set(maze["barriers"])
)

print("Visited node:", result["visited_order"])
print("Time taken:", result["time_taken"])
print("Final path:", result["final path"])

if result["final path"] is not None:
    total_cost = 0
    print("\nEdge costs along final path:")

    for i in range(len(result["final path"]) - 1):
        n1 = result["final path"][i]
        n2 = result["final path"][i + 1]
        cost = edge_cost(n1, n2)
        total_cost += cost
        print(f"{n1} -> {n2} : {cost:.3f}")

    print("Total path cost:", round(total_cost, 3))