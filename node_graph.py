import grid_map as gm
import networkx as nx

class node():
    def __init__(self,id):
        self.id = id
        self.space = []
        self.child = []
        self.parent = []
    def add_slice(self, line_slide):
        self.space.append(line_slide)
        

class node_graph:
    def __init__(self,grid_map):
        self.grid_map = grid_map
        self.rows = len(grid_map.map_data)
        self.cols = len(grid_map.map_data[0])

    def check_connect(self, a, b):
        if a[0].col >= b[0].col:
            x = a[0].col
            vmin = b[0].col
            vmax = b[len(b)-1].col
        else:
            x = b[0].col
            vmin = a[0].col
            vmax = a[len(b)-1].col
        if x >= vmin and x<= vmax:
            return True
        return False
            

    def create_graph(self):
        G = nx.DiGraph()
        slices = []
        pre_line_slides = []
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

            if len(pre_line_slides) != 0:
                for i in range(len(pre_line_slides)):
                    offset = len(pre_line_slides)
                    pre = pre_line_slides[i]
                    G.add_node(i)
                    for j in range(len(cur_line_slides)):
                        cur = cur_line_slides[j]
                        G.add_node(j  + offset)
                        if self.check_connect(pre,cur):
                            G.add_edge(i, j + offset)
            pre_line_slides = cur_line_slides
        print slices
