from IPython.display import HTML, Image
from js2py import eval_js
from base64 import b64decode
import PIL
import project1part2
import numpy as np
import vis

def find_points(image_array, pixels):
    points = []
    for grid_i, i in enumerate(range (10, image_array.shape[0]-10, 20)):
        for grid_j, j in enumerate(range (10, image_array.shape[1]-10, 20)):
            if np.array_equal(image_array[i][j], pixels):
                points.append([grid_i+1, grid_j+1])
    return points

def load_maze(fname='/content/drawing.png'):
    N = 17
    image = PIL.Image.open(fname)
    image_array = np.round(np.array(image)/255)

    start_x, start_y = find_points(image_array, [0,1,0,1])[0]
    end_x, end_y = find_points(image_array, [1, 0, 0, 1])[0]
    walls = find_points(image_array, [0, 0, 0, 1])
    new_grid = project1part2.project1part1.Maze(N, (start_x, start_y), (end_x, end_y))

    for i in range(N):
        for j in range(N):
            if [i, j] in walls:
                new_grid.grid[i,j] = 0
            else:
                new_grid.grid[i, j] = 1

    g = new_grid
    g.draw_map()
    return g
def my_function(a, b):
    return abs(a[0] - b[0]) + abs(a[1] - b[1])
def all_cost_1(a,b):
    return 1
def all_cost_0(a,b):
    return 0
    N=40
def fun(a,b):
  return abs(a[1] - b[1])
name_pic=('ko')
g = load_maze(name_pic+'.png')
pf = project1part2.Pathfinder(g, c=project1part2.all_cost_1, h=project1part2.manhatan)   # change arguments to choose the appropriate pathfinding algorithm and cost/heuristic (if applicable)
g.draw_map(pf.get_path())
pf.vis.save_gif('new'+name_pic+'.gif')