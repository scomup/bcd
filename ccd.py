from enum import Enum
import numpy as np
import matplotlib.pyplot as plt
import grid_map as gm
import node_graph as ng

import operator


def update_v(rows,cols,map_data,v_data):
    for i in range(rows):
        for j in range(cols):
            v_data[i,j] = map_data[i][j].h                      

ROBOT_SIZE = 3
rows = 20
cols = 20
g = gm.grid_map(rows,cols)
g.init_map()
g.update_weight(ROBOT_SIZE)
graph = ng.node_graph(g)
graph.create_graph()
fig,ax=plt.subplots()
ax.set_aspect('equal')
ax.pcolor(g.v_data,cmap=plt.cm.Reds,edgecolors='k')

plt.show()
