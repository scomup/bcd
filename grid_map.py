from enum import Enum
import numpy as np
import matplotlib.pyplot as plt

INF = float("inf")
INF = 200
BIG = 100
BIG_2 = BIG/2
class Stat(Enum):
    FREE = 0
    OBSTACLE = 1

class Tag(Enum):
    NEW = 0
    OPEN = 1
    CLOSE = 2

class map_cell:
    def __init__(self,row,col):
        
        self.back_point = self
        self.path = False
        self.tag = Tag.NEW
        self.stat = Stat.FREE
        self.h = 0
        self.k = 0
        self.weight = 0
        self.visited = 0
        self.row = row
        self.col = col

    def cost(self,to_ceil):                  
        a = abs(to_ceil.row - self.row)
        b = abs(to_ceil.col - self.col)
        if a > 1 or b > 1:
            print 'COST ERROR'
            return -1
        elif to_ceil.stat  == Stat.OBSTACLE or self.stat == Stat.OBSTACLE:
            return INF
        elif a == 0 or b == 0:
            return 1
        else:
            return 2

class grid_map:
    def __init__(self,rows,cols):
        self.rows = rows
        self.cols = cols
        self.map_data = []
        self.v_data = np.zeros((rows, cols))
        self.v_data.fill(Stat.FREE)
        for i in range(rows):
            line = []
            for j in range(cols):
                cell = map_cell(i,j)
                line.append(cell)
            self.map_data.append(line)

    def nearby(self,cell,radius):
        row_l = max(cell.row - radius, 0)
        row_h = min(cell.row + radius + 1, self.rows )
        col_l = max(cell.col - radius, 0)
        col_h = min(cell.col + radius + 1, self.cols )
        tmp = []
        for i in range(row_l, row_h):
            tmp.extend(self.map_data[i][col_l : col_h])
        #del tmp[(radius*2+1)*radius + radius]
        return tmp
    def distance(self,cell_a,cell_b):
        a = abs(cell_a.row - cell_b.row) 
        b = abs(cell_a.col - cell_b.col)
        return max(a, b)          
    def update_weight(self,radius):
        for i in range(self.rows):
            for j in range(self.cols):
                cell_current = self.map_data[i][j]
                if cell_current.stat == Stat.OBSTACLE: 
                    cell_current.weight = BIG
                    # update v for visulization
                    self.v_data[cell_current.row,cell_current.col] = cell_current.weight
                    nearby = self.nearby(cell_current,2 * radius + 1)
                    for cell in nearby:
                        d = self.distance(cell_current, cell)
                        if d <=  radius:
                            weight = BIG_2
                        else:
                            weight = 8 - d
                        cell.weight = max(cell.weight, weight)
                        # update v for visulization
                        self.v_data[cell.row,cell.col] = cell.weight                      
        

    def set_goal(self,row,col):
        self.goal = self.map_data[row][col]
        
    def set_start(self,row,col):
        self.start = self.map_data[row][col]

    def init_map(self):
        self.map_data[16][11].stat = Stat.OBSTACLE
        self.map_data[16][12].stat = Stat.OBSTACLE
        self.map_data[16][13].stat = Stat.OBSTACLE
        self.map_data[16][14].stat = Stat.OBSTACLE
    
        self.map_data[15][5].stat = Stat.OBSTACLE
        self.map_data[15][6].stat = Stat.OBSTACLE
        self.map_data[15][7].stat = Stat.OBSTACLE
        self.map_data[15][8].stat = Stat.OBSTACLE
        self.map_data[15][9].stat = Stat.OBSTACLE
        #self.map_data[15][10].stat = Stat.OBSTACLE
        self.map_data[15][11].stat = Stat.OBSTACLE
        self.map_data[15][12].stat = Stat.OBSTACLE
        self.map_data[15][13].stat = Stat.OBSTACLE
        self.map_data[15][14].stat = Stat.OBSTACLE

        self.map_data[14][5].stat = Stat.OBSTACLE
        self.map_data[14][6].stat = Stat.OBSTACLE
        self.map_data[14][7].stat = Stat.OBSTACLE
        self.map_data[14][8].stat = Stat.OBSTACLE
        self.map_data[14][9].stat = Stat.OBSTACLE
        #self.map_data[14][10].stat = Stat.OBSTACLE
        self.map_data[14][11].stat = Stat.OBSTACLE
        self.map_data[14][12].stat = Stat.OBSTACLE
        self.map_data[14][13].stat = Stat.OBSTACLE
        self.map_data[14][14].stat = Stat.OBSTACLE

        self.map_data[13][5].stat = Stat.OBSTACLE
        self.map_data[13][6].stat = Stat.OBSTACLE
        self.map_data[13][7].stat = Stat.OBSTACLE
        self.map_data[13][8].stat = Stat.OBSTACLE
        self.map_data[13][9].stat = Stat.OBSTACLE
        #self.map_data[13][10].stat = Stat.OBSTACLE
        self.map_data[13][11].stat = Stat.OBSTACLE
        self.map_data[13][12].stat = Stat.OBSTACLE
        self.map_data[13][13].stat = Stat.OBSTACLE
        self.map_data[13][14].stat = Stat.OBSTACLE

        self.map_data[12][5].stat = Stat.OBSTACLE
        self.map_data[12][6].stat = Stat.OBSTACLE
        self.map_data[12][7].stat = Stat.OBSTACLE
        self.map_data[12][8].stat = Stat.OBSTACLE
        self.map_data[12][9].stat = Stat.OBSTACLE
        #self.map_data[12][10].stat = Stat.OBSTACLE
        self.map_data[12][11].stat = Stat.OBSTACLE
        self.map_data[12][12].stat = Stat.OBSTACLE
        self.map_data[12][13].stat = Stat.OBSTACLE
        self.map_data[12][14].stat = Stat.OBSTACLE

        self.map_data[11][5].stat = Stat.OBSTACLE
        self.map_data[11][6].stat = Stat.OBSTACLE
        self.map_data[11][7].stat = Stat.OBSTACLE
        self.map_data[11][8].stat = Stat.OBSTACLE
        self.map_data[11][9].stat = Stat.OBSTACLE
        #self.map_data[11][10].stat = Stat.OBSTACLE
        self.map_data[11][11].stat = Stat.OBSTACLE
        self.map_data[11][12].stat = Stat.OBSTACLE
        self.map_data[11][13].stat = Stat.OBSTACLE
        self.map_data[11][14].stat = Stat.OBSTACLE

        self.map_data[10][5].stat = Stat.OBSTACLE
        self.map_data[10][6].stat = Stat.OBSTACLE
        self.map_data[10][7].stat = Stat.OBSTACLE
        self.map_data[10][8].stat = Stat.OBSTACLE
        self.map_data[10][9].stat = Stat.OBSTACLE
        #self.map_data[10][10].stat = Stat.OBSTACLE
        self.map_data[10][11].stat = Stat.OBSTACLE
        self.map_data[10][12].stat = Stat.OBSTACLE
        self.map_data[10][13].stat = Stat.OBSTACLE
        self.map_data[10][14].stat = Stat.OBSTACLE

        self.map_data[3][14].stat = Stat.OBSTACLE
        self.map_data[3][15].stat = Stat.OBSTACLE
        self.map_data[4][13].stat = Stat.OBSTACLE
        self.map_data[4][14].stat = Stat.OBSTACLE
        self.map_data[4][15].stat = Stat.OBSTACLE
        self.map_data[4][16].stat = Stat.OBSTACLE
        self.map_data[5][13].stat = Stat.OBSTACLE
        self.map_data[5][14].stat = Stat.OBSTACLE
        self.map_data[5][15].stat = Stat.OBSTACLE
        self.map_data[5][16].stat = Stat.OBSTACLE
        self.map_data[6][14].stat = Stat.OBSTACLE
        self.map_data[6][15].stat = Stat.OBSTACLE
    