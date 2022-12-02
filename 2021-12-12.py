# https://adventofcode.com/2021/day/12

from pathlib import Path
import networkx as nx
import matplotlib.pyplot as plt

filename = f"input_" + Path(__file__).stem + ".txt"
filepath = Path(filename)

nodes = set()
edges = set()

with filepath.open("r") as stream:
    for line in stream:
        node1, node2 = line.strip("\n").split("-")
        edge = frozenset((node1, node2))
        nodes.update(edge)
        edges.add(edge)

graph = nx.Graph()

graph.add_nodes_from(nodes)
graph.add_edges_from(edges)

nx.draw(graph, with_labels=True)
plt.show()
