import grid_map as gm
import networkx as nx
import matplotlib.pyplot as plt

class node():
    def __init__(self,id, vmin, vmax):
        self.id = id
        self.vmin = vmin
        self.vmax = vmax
        self.child = []
        self.parent = []
        self.space = []
    def add_slice(self, line_slide):
        self.space.append(line_slide)
        

class node_graph:
    def __init__(self,grid_map):
        self.grid_map = grid_map
        self.rows = len(grid_map.map_data)
        self.cols = len(grid_map.map_data[0])
        self.open = []
        self.close = []
        self.create_node_list()
        self.create_graph()

    def create_graph(self):
        G=nx.Graph()
        for n in self.close:
            G.add_node(n.id, pt=n)
        for n in self.close:
            for c in n.child:
                G.add_edge(n.id,c.id)
        nx.draw(G)
        #plt.show()

        
    def check_connect(self, a, b):
        if a.vmin >= b.vmin:
            x = a.vmin
            vmin = b.vmin
            vmax = b.vmax
        else:
            x = b.vmin
            vmin = a.vmin      
            vmax = a.vmax
        if x >= vmin and x<= vmax:
            return True
        return False
            

    def create_node_list(self):
        slices = []
        idx = 0
        first_flag = 1
        for line in self.grid_map.map_data:
            open_flag = 0
            cur_line_slides = []
            line_slide = []
            for cell in line:
                if (open_flag == 0) and (cell.stat == gm.Stat.FREE):
                    open_flag = 1
                    line_slide.append(cell)
                elif open_flag and (cell.stat == gm.Stat.FREE):
                    line_slide.append(cell)
                elif open_flag and (cell.stat == gm.Stat.OBSTACLE):
                    open_flag = 0
                    cur_line_slides.append(line_slide)
                    line_slide = []
            if open_flag:
                cur_line_slides.append(line_slide)

            if first_flag == 0:
                tmp_idx = 0
                tmp_nodes = []
                for i in cur_line_slides:
                    n = node(tmp_idx, i[0].col, i[len(i) - 1].col)
                    tmp_idx = tmp_idx + 1
                    n.space.append(i)
                    tmp_nodes.append(n)
                for tn in tmp_nodes:
                    for n in self.open:
                        if self.check_connect(tn, n):
                            tn.parent.append(n)
                            n.child.append(tn)

                for n in self.open:
                    if len(n.child) == 0:
                        if self.open.count(n):
                            self.open.remove(n)
                        self.close.append(n)

                for tn in tmp_nodes:
                    if len(tn.parent) == 1 and len(tn.parent[0].child) == 1:
                        n.vmax = tn.vmax
                        n.vmin = tn.vmin
                        tn.parent[0].child = []
                        tn.parent[0].space.append(tn.space[0])
                       
                    elif len(tn.parent) == 1 and len(tn.parent[0].child) > 1:
                        if self.open.count(tn.parent[0]):
                            self.open.remove(tn.parent[0])
                            self.close.append(tn.parent[0])
                        tn.id = idx
                        idx = idx + 1
                        self.open.append(tn)
                        tn.child = []
                    elif len(tn.parent) == 0:
                        tn.id = idx
                        idx = idx + 1
                        self.open.append(tn)
                    elif  len(tn.parent) > 1:
                        for p in tn.parent:
                             if self.open.count(p):
                                self.open.remove(p)
                                self.close.append(p)
                        tn.id = idx
                        idx = idx + 1
                        self.open.append(tn)
            else:
                for i in cur_line_slides:
                    first_flag  = 0
                    n = node(idx, i[0].col, i[len(i) - 1].col)
                    idx = idx + 1
                    n.space.append(i)
                    self.open.append(n)
        for n in self.open:
            self.close.append(n)
        print slices
