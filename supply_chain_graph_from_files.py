import networkx as nx
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

node_file = open("supply_chain_nodes.txt", 'r')
data = node_file.read()

node_list = data.split('\n')
node_list.pop()
node_file.close()

edge_matrix = np.genfromtxt("supply_chain_edges.csv", delimiter=',')

supply_network = pd.DataFrame(edge_matrix, index=node_list, columns=node_list)

nx.draw_networkx(nx.from_pandas_adjacency(supply_network), with_labels=True)
plt.show()
