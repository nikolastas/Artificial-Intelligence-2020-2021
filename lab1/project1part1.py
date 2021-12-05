import numpy as np
from queue import LifoQueue
import  random 
import matplotlib.pyplot as plt


class Maze:
    def __init__(self, N, S, F):

      """
      N: integer that indicates the size of the NxN grid of the maze
      S: pair of integers that indicates the coordinates of the starting point (S)
      F: pair of integers that indicates the coordinates of the finish point (F)
      You can add any other parameters you want to customize maze creation (e.g. variables that
      control the creation of additional paths)
      """

      assert N > 2

      ## Make sure start and end are within the grid

      assert S[0] < N-1
      assert S[1] < N-1
      assert F[0] < N-1
      assert F[1] < N-1

      assert S[0] > 0
      assert S[1] > 0
      assert F[0] > 0
      assert F[1] > 0

      # Add here any additional constraints your implementation may have

      self.N = N
      self.S = S
      self.F = F

      # Grid initialized with obstacles (array of 0/False)
      # 1/True indicates available cells
      self.grid = np.zeros((N, N), dtype=bool)
      
      ## YOUR CODE HERE      
      (x,y)=S
        
      visited=[S]
      stack=[]
      stack.append(S)
        
      
      while(stack):
            n=[]
            thesigeitona=[]
            current=stack.pop()
            Maze.neighbours(current, visited, n, N,thesigeitona) #vriskei toys geitones toy current kai toys vazei sto thesigeitona 
            #sto n vazei ta endiamesa tou current kai toy thesigeitona
            if(n):
                  stack.append(current)
                  randomNeighbour=random.choice(thesigeitona)
                  endiamesh=n[thesigeitona.index(randomNeighbour)]
                  self.grid[randomNeighbour]=True
                  self.grid[endiamesh]=True
                  self.grid[current]=True
                  visited.append(randomNeighbour)
                  #visited.append(current)
                  stack.append(randomNeighbour)
            (x,y)=F
            if(self.grid[x-1,y]==False and self.grid[x+1,y]==False and self.grid[x,y-1]==False and self.grid[x,y+1]==False and stack==[]):
                  self.grid = np.zeros((N, N), dtype=bool)
                  visited=[S]
                  stack=[]
                  stack.append(S)
      #=================== standard algorithm ====================
      """l=[]
      stop=False
      for i in range(1,N-1):
        for j in range(1,N-1):
          if(self.grid[i,j]== True):
                continue

          
          if(not stop and (self.grid[i-1,j]==True and self.grid[i+1,j]==True)):
                self.grid[i,j]=True
                stop=True
          if(not stop and (self.grid[i,j-1]==True and self.grid[i,j+1]==True)):
                self.grid[i,j]=True
                stop=True
          if(stop):
                break
        if stop:
              break"""

                
          #if(self.grid[i,j]==False and ((self.grid[i-1,j]==True and self.grid[i+1,j]==True) or  (self.grid[i,j-1]==True and self.grid[i,j+1]==True) ) ): #search for bloacked blocks which have passes before and after them
                #l.append((i,j)) # put them in a list
      #random_number_of_blocks=random.randint(1, len(l)//2) # pick a random number from 1 to len(l)/2
      #while(random_number_of_blocks):
            #self.grid[random.choice(l)]=True #make them passes
            #random_number_of_blocks-=1 
      # now to go from S to F i must have above 2 ways       
                                
          
          
    
    
      ## CODE END
    def valid(k,N):
        (x,y)=k
        if  ((x<N) and (x>0) and (y<N) and (y>0) ) :
            return True  
        else :
            return False       
    def neighbours(k,visited,endiameshthesi,N,thesigeitona):
          (i,j)=k
          (x,y)=(i-2,j)
          #print("x,y=",x,y,"check for valid=",Maze.valid((x,y),self))
          if(Maze.valid((x,y),N) and Maze.valid((i-1,j),N)and  ((x,y) not in visited)):
            endiameshthesi.append((i-1,j))
            thesigeitona.append((x,y))
          (x,y)=(i+2,j)
          #print("x,y=",x,y,"check for valid=",Maze.valid((x,y),self))
          if( Maze.valid((x,y),N) and Maze.valid((i+1,j),N) and (x,y) not in visited):
            endiameshthesi.append((i+1,j))
            thesigeitona.append((x,y))
          (x,y)=(i,j-2)
          #print("x,y=",x,y,"check for valid=",Maze.valid((x,y),self))
          if(Maze.valid((x,y),N )and Maze.valid((i,j-1),N)and (x,y) not in visited):
            endiameshthesi.append((i,j-1))
            thesigeitona.append((x,y))
          (x,y)=(i,j+2)
          #print("x,y=",x,y,"check for valid=",Maze.valid((x,y),self))
          if(Maze.valid((x,y),N) and Maze.valid((i,j+1),N) and ((x,y) not in visited )):
            endiameshthesi.append((i,j+1))
            thesigeitona.append((x,y))
          #print("neighbours checked for",k," = ",thesigeitona,)


    def draw_map(self, path=None):
        """ Draws the maze as an image. Considers grid values of 0/False to represent obstacles and
        values of 1/True to represent empty cells, but this can be customized. Obstacles are painted
        black and empty cells are painted white. Starting point is painted green and finish point red.
        Optionally accepts as a parameter a path within the maze which is painted blue. 
        """
        image = np.zeros((self.N, self.N, 3), dtype=int)
        image[~self.grid] = [0, 0, 0]
        image[self.grid] = [255, 255, 255]

        # Uncomment the next 2 lines of code to treat 1/True as obstacles (and 0/False as free maze cells)
        # image[self.grid] = [0, 0, 0]
        # image[~self.grid] = [255, 255, 255]

        image[self.S] = [50, 168, 64]
        image[self.F] = [168, 50, 50]
        if path:
            for n in path[1:-1]:
                image[n] = [66, 221, 245]

        plt.imshow(image)
        plt.xticks([])
        plt.yticks([])
        plt.show()
map = Maze(11, (1,1),(8,8))
map.draw_map()
