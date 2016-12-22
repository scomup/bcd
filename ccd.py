from enum import Enum
import numpy as np
import matplotlib.pyplot as plt
import grid_map as gm
import node_graph as ng

import operator


def update_v(rows,cols,nodes,v_data):
    color = 1
    for node in nodes:
        color = color + 1
        for line in node.space:
            for cell in line:
                v_data[cell.row,cell.col] = color                

ROBOT_SIZE = 3
rows = 20
cols = 20
g = gm.grid_map(rows,cols)
g.init_map()
g.update_weight(ROBOT_SIZE)
graph = ng.node_graph(g)
nodes = graph.close
fig,ax=plt.subplots()
ax.set_aspect('equal')
v_data = np.zeros((rows, cols))
update_v(rows,cols,nodes,v_data)
#ax.pcolor(v_data,cmap=plt.cm.Reds,edgecolors='k')
ax.pcolor(v_data,edgecolors='k')
plt.show()
