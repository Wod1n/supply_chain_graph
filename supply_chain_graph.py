import networkx as nx
import matplotlib.pyplot as plt
import numpy as np

supply_network = nx.Graph()
supply_network.add_node("UK")
supply_network.add_node("Gibraltar")
supply_network.add_node("Halifax")
supply_network.add_node("Bermuda")
supply_network.add_edge("UK", "Gibraltar")
supply_network.add_edge("UK", "Halifax")
supply_network.add_edge("UK", "Bermuda")

supply_network.add_node("Cyprus")
supply_network.add_node("Suez")
supply_network.add_node("Duqm")

supply_network.add_edge("Gibraltar", "Cyprus")
supply_network.add_edge("Gibraltar", "Suez")
supply_network.add_edge("Cyprus", "Suez")

supply_network.add_edge("Suez", "Duqm")

supply_network.add_node("Baharain")
supply_network.add_node("Diego Garcia")

supply_network.add_edge("Duqm", "Baharain")
supply_network.add_edge("Duqm", "Diego Garcia")

supply_network.add_node("Brisbane")
supply_network.add_node("Singapore")
supply_network.add_node("New Caledonia")
supply_network.add_node("Perth")
supply_network.add_node("Sydney")

supply_network.add_edge("Diego Garcia", "Singapore")
supply_network.add_edge("Diego Garcia", "Brisbane")
supply_network.add_edge("Diego Garcia", "Perth")
supply_network.add_edge("Brisbane", "Perth")
supply_network.add_edge("Perth", "Sydney")
supply_network.add_edge("Sydney", "Brisbane")

supply_network.add_edge("New Caledonia", "Sydney")
supply_network.add_edge("New Caledonia", "Brisbane")
supply_network.add_edge("New Caledonia", "Singapore")

supply_network.add_node("Ascension Island")
supply_network.add_node("Falkland Islands")
supply_network.add_node("Table Bay")
supply_network.add_node("Panama")
supply_network.add_node("Hawaii")

supply_network.add_edge("Halifax", "Bermuda")
supply_network.add_edge("Gibraltar", "Ascension Island")
supply_network.add_edge("Bermuda", "Ascension Island")
supply_network.add_edge("Ascension Island", "Falkland Islands")
supply_network.add_edge("Ascension Island", "Table Bay")
supply_network.add_edge("Falkland Islands", "Table Bay")

supply_network.add_edge("Bermuda", "Panama")
supply_network.add_edge("Panama", "New Caledonia")
supply_network.add_edge("Panama", "Hawaii")
supply_network.add_edge("Hawaii", "Singapore")

''''
home_node = "UK"
center_node = "Ascension Islands"
middle_east = "Duqm"
far_east = "Singapore"

sub_nodes = set(supply_network) - {home_node, center_node, middle_east, far_east}
pos = nx.spring_layout(sub_nodes)
pos[center_node] = np.array([-14, -8])
pos[home_node] = np.array([-3, 55])
pos[middle_east] = np.array([58, 20])
pos[far_east] = np.array([104, 1])
'''

nx.draw(supply_network, with_labels=True)
plt.show()
