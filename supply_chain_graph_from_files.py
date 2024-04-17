import json
import networkx as nx
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

def make_graph(node_file_name, edge_file_name):
    node_file = open(node_file_name, 'r')
    data = node_file.read()
    node_list = data.split('\n')
    node_list.pop()
    node_file.close()

    edge_matrix = np.genfromtxt(edge_file_name, delimiter=',')
    graph_table = pd.DataFrame(edge_matrix, index=node_list, columns=node_list)
    graph = nx.from_pandas_adjacency(graph_table)
    #graph = nx.from_numpy_array(edge_matrix, create_using=nx.MultiGraph)
    #nx.draw_networkx(graph, with_labels=True)
    #plt.show()
    return graph

atlantic_graph = make_graph("atlantic_nodes.txt", "atlantic_edges.csv")
med_graph = make_graph("med_nodes.txt", "med_edges.csv")
aus_graph = make_graph("aus_nodes.txt", "aus_edges.csv")
pacific_graph = make_graph("pacific_nodes.txt", "pacific_edges.csv")
indian_graph = make_graph("indian_nodes.txt", "indian_edges.csv")

western_graph = nx.compose(atlantic_graph, med_graph)
eastern_graph = nx.compose(pacific_graph, aus_graph)

supply_graph = nx.compose(western_graph, indian_graph)

with open("node_coords.json") as json_file:
    pos = json.load(json_file)

for x in pos.keys():
    pos[x].reverse()
supply_graph = nx.compose(supply_graph, eastern_graph)
nx.draw(supply_graph, pos, with_labels=True)
plt.show()
#nx.draw_networkx(supply_graph, with_labels=True)
#plt.show()
