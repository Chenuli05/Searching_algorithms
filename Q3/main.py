from maze import *
from search_iddfs import *
from best_first_search import *

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
print("Time taken:", result["time_taken"], "minutes")
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
    print()
#viewing the heuristic cost for each node
    h = chebyshev_distance(maze["start"], maze["goal"])
    print("Heuristic cost of start node:", h)

    print("Heuristic from start to goal:", chebyshev_distance(maze["start"], maze["goal"]))

    for node in [maze["start"], 7, 13, 20]:
        print(f"h({node}) = {chebyshev_distance(node, maze['goal'])}")

best_first_result = best_first_search(
    start=maze["start"],
    goal=maze["goal"],
    barriers=set(maze["barriers"]),
)
print("\nBest first search result:")
print("Visited node:", best_first_result["visited_nodes"])
print("Time taken:", best_first_result["time_taken"], "minutes")
print("Final path:", best_first_result["final_path"])