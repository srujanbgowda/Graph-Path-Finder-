
graph_input = {
    "nodes": ["A", "B", "C", "D", "E", "F"],
    "edges": [
        ("A", "B", 1),
        ("A", "C", 2),
        ("B", "D", 3),
        ("C", "E", 4),
        ("D", "F", 2),
        ("E", "F", 1),
    ],
    "directed": False,
    "start": "A",
    "end": "F",
}

def weight_of(u, v, edges, undirected=True):
    for a, b, w in edges:
        if (a == u and b == v) or (undirected and a == v and b == u):
            return w
    return "?"

def print_graph_info(g):
    print("Nodes:", g["nodes"])
    print("Edges:", g["edges"])
    print("Directed:", g["directed"])
    print("Query:", g["start"], "->", g["end"])
    print()

def print_ascii_diagram(g):
    # This layout matches your A–B/C–D/E–F shape
    wAB = weight_of("A", "B", g["edges"], undirected=not g["directed"])
    wAC = weight_of("A", "C", g["edges"], undirected=not g["directed"])
    wBD = weight_of("B", "D", g["edges"], undirected=not g["directed"])
    wCE = weight_of("C", "E", g["edges"], undirected=not g["directed"])
    wDF = weight_of("D", "F", g["edges"], undirected=not g["directed"])
    wEF = weight_of("E", "F", g["edges"], undirected=not g["directed"])

    diagram = f"""
    A
   / \\
 ({wAB}) ({wAC})
 /       \\
B         C
|         |
({wBD})  ({wCE})
|         |
D         E
 \\       /
 ({wDF}) ({wEF})
   \\   /
     F
"""
    print("Graph Diagram:")
    print(diagram)

if __name__ == "__main__":
    print_graph_info(graph_input)
    print_ascii_diagram(graph_input)
