

import numpy as np
import project1part1 
import vis

#============================= visualization =============================
class Pathfinder:
    def __init__(self, maze, c, h):
        """
        maze : Αντικείμενο τύπου Maze (από Μέρος 1)
        c : Συνάρτηση που υπολογίζει την πραγματική απόσταση μεταξύ δύο σημείων
        h : Συνάρτηση που υπολογίζει την ευριστική μεταξύ δύο σημείων
        """
        self.maze = maze
        self.vis = vis.visualization(maze.S, maze.F)
        self.path = []
        self.cost = c
        self.heuristic = h
        
        
    ### Fill the path list with the coordinates of each point in the path from maze.S to maze.F
    ### Your code here
        self.exp=[]
        N=maze.N
        openset = set()
        closedset = set()
        #Current point is the starting point
        curent = maze.S
        #Add the starting point to the open set
        openset.add(curent)
        #While the open set is not empty
        gcost={}
        gcost[maze.S]=0
        fcost={}
        fcost[maze.S]=self.heuristic(maze.S,maze.F)
        cameFrom={}

        self.vis.draw_step(maze, Pathfinder.sm2list(openset), Pathfinder.sm2list(closedset))
        #self.vis.show_last_frame()
        #self.vis.create_gif()
        while openset:
            
            self.vis.draw_step(maze, Pathfinder.sm2list(openset), Pathfinder.sm2list(closedset))
            
            
            
            self.vis.create_gif()
            
            
            
            #Find the item in the open set with the lowest G + H score
            curent=None
            for block in openset:
                if(curent==None or fcost[block] < fcost[curent]):
                    #print(block," -> ", fcost[block])
                    curent=block

            #If it is the item we want, retrace the path and return it
            if curent == maze.F:
                cell=maze.F
                self.path.append(cell)
                while(cell!=maze.S):
                    self.path.append(cameFrom[cell])
                    cell=cameFrom[cell]
                #print(self.path)
                break
            #Remove the item from the open set
            if (curent==None):
                #print("Path does not exist!")
                break
            
                #print("current is ", curent)
                
            
            
            #Add it to the closed set
            #print("curent=",curent," has child ",Pathfinder.next_neightbours(maze, N, curent))
            #Loop through the node's children/siblings
            for node in Pathfinder.next_neightbours(maze, N, curent):
                if node not in closedset and node not in openset :
                    #If it isn't in the open nor the closed set, calculate the G and H score for the node
                    #node.G = current.G + current.move_cost(node)
                    (x,y)=node
                    
                    gcost[node]=gcost[curent]+self.cost(node,curent)
                    #node.H = manhattan(node, goal)
                    
                    fcost[node]=gcost[node]+self.heuristic(node,maze.F)
                    #Set the parent to our current item
                    #node.parent = current
                    cameFrom[node]=curent
                    
                    #Add it to the set
                    openset.add(node)
                
                else:
                    #Check if we beat the G score
                    (x,y)=node 
                    
                    new_f = gcost[curent] + self.cost(curent,node) + self.heuristic(node,maze.F)
                    
                    if fcost[node] > new_f:
                        #If so, update the node to have a new parent 
                        #And update the new G cost
                        del fcost[node]
                        fcost[node] = new_f
                        del gcost[node]
                        gcost[node]=gcost[curent] + self.cost(curent,node)
                        del cameFrom[node]
                        cameFrom[node]=curent
                        #if the node is in closedset then you have to search again for the best path :(, so put it in the open set
                        if node in closedset:
                            closedset.remove(node)
                            openset.add(node)
        #ani=self.vis.save_gif("new.gif") -------------------------------------------------------------------       
            openset.remove(curent)
            closedset.add(curent)
        self.exp=len(closedset)
        
            
                
          
    def dict2list(d,curent,maze):
        l=[]
        cell=curent
        l.append(cell)
        while(cell!=maze.S):
            l.append(d[cell])
            cell=d[cell]
        return l


    def sm2list(k):
        l=[]
        for i in k:
            l.append(i)
        return l   
    def valid(k,N):
        (x,y)=k
        if  ((x<N) and (x>0) and (y<N) and (y>0) ) :
            return True  
        else :
            return False    
    def distance(heuristic, cost, current):
        (x,y)=current
        return heuristic(current,maze.F)+ cost(x,y)
    def next_neightbours(maze,N,curent): #working
          (i,j)=curent
          N=maze.N
          (x,y)=(i-1,j)
          l=[]
          #print("x,y=",x,y,"check for valid=",Maze.valid((x,y),self))
          if(Pathfinder.valid((x,y),N)  and (maze.grid[(x,y)]==True or (x,y)== maze.F) ):
            l.append((x,y))
          (x,y)=(i+1,j)
          #print("x,y=",x,y,"check for valid=",Maze.valid((x,y),self))
          if( Pathfinder.valid((x,y),N)  and (maze.grid[(x,y)]==True or (x,y)== maze.F)):
            l.append((x,y))
          (x,y)=(i,j-1)
          #print("x,y=",x,y,"check for valid=",Maze.valid((x,y),self))
          if(Pathfinder.valid((x,y),N )and (maze.grid[(x,y)]==True or (x,y)== maze.F)):
            l.append((x,y))
          (x,y)=(i,j+1)
          #print("x,y=",x,y,"check for valid=",Maze.valid((x,y),self))
          if(Pathfinder.valid((x,y),N)  and (maze.grid[(x,y)]==True or (x,y)== maze.F)):
            l.append((x,y))
          
          return l
    def get_path(self):
        return self.path
    def get_exp(self):
        return self.exp
import math

## A heuristic
def manhatan(a, b):
    return abs(a[0] - b[0]) + abs(a[1] - b[1])
def all_cost_1(a,b):
    return 1
def all_cost_0(a,b):
  return 0
def euclidean(a,b):
  return math.sqrt(math.pow((a[0]-b[0]),2)+math.pow((a[1]-b[1]),2))
## Create a 41x41 maze
"""N = 20
S = (2, 2)
F = (18, 12)
maze = project1part1.Maze(N, S, F)
## Find and visualize the path

pf = Pathfinder(maze=maze, c = all_cost_1, h = manhatan)
maze.draw_map(pf.get_path())"""