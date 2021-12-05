

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
        while openset:
            self.vis.draw_step(maze, openset, closedset)
            #self.vis.show_last_frame()
            ani = self.vis.create_gif()
            
            anim= self.vis.show_gif()
            #self.vis.create_gif()
            #self.vis.show_gif()
            
            #print(openset)
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
            else:
                #print("current is ", curent)
                openset.remove(curent)
                closedset.add(curent)
            
            
            #Add it to the closed set
            #print("curent=",curent," has child ",Pathfinder.next_neightbours(maze, N, curent))
            #Loop through the node's children/siblings
            for node in Pathfinder.next_neightbours(maze, N, curent):
                #If it is already in the closed set, skip it
                if node in closedset:
                    continue
                #Otherwise if it is already in the open set
                if node in openset:
                    #Check if we beat the G score
                    (x,y)=node 
                    
                    new_g = gcost[curent] + self.cost(curent,node)
                    
                    if gcost[node] > new_g:
                        #If so, update the node to have a new parent
                        del gcost[node]
                        gcost[node] = new_g
                        del cameFrom[node]
                        cameFrom[node]=curent
                else :
                    #If it isn't in the open set, calculate the G and H score for the node
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
import math

## A heuristic
def my_function(a, b):
    return abs(a[0] - b[0]) + abs(a[1] - b[1])
def all_1(a,b):
    return 1
## Create a 41x41 maze
N = 150
S = (5, 9)
F = (137, 37)
maze = project1part1.Maze(N, S, F)
## Find and visualize the path

pf = Pathfinder(maze=maze, c = all_1, h = my_function)
maze.draw_map(pf.get_path())