import project1part2
import random
import project1part1
import matplotlib.pyplot as plt

fpath_lengths_a = []
fexp_nodes_a=[]
fpath_lengths_b = []
fexp_nodes_b=[]
fpath_lengths_c = []
fexp_nodes_c=[]
map_sizes = [10,20,30,40,50,60,70,80,90]
def my_function(a, b):
    return abs(a[0] - b[0]) + abs(a[1] - b[1])
def all_cost_1(a,b):
    return 1
def all_cost_0(a,b):
    return 0
for i in map_sizes:
    path_length_a=0
    exp_length_a=0
    path_length_b=0
    exp_length_b=0
    path_length_c=0
    exp_length_c=0

    for j in range(1,11):
        
        S=(1,1)
        
        F=(i-2,i-2)
        
        N=i
        maze = project1part2.project1part1.Maze(N, S, F)
        pf_a = project1part2.Pathfinder(maze, c= all_cost_0, h=my_function)
        pf_b = project1part2.Pathfinder(maze, c= all_cost_1, h=all_cost_0)
        pf_c = project1part2.Pathfinder(maze, c= all_cost_1, h=my_function)
        path_length_a+=len(pf_a.get_path())
        exp_length_a+=pf_a.get_exp()
        path_length_b+=len(pf_b.get_path())
        exp_length_b+=pf_b.get_exp()
        path_length_c+=len(pf_c.get_path())
        exp_length_c+=pf_c.get_exp()
    
    exp_length_a/=10
    path_length_a/=10
    exp_length_b/=10
    path_length_b/=10
    exp_length_c/=10
    path_length_c/=10
    fpath_lengths_a.append( path_length_a)
    fpath_lengths_b.append( path_length_b)
    fexp_nodes_a.append( exp_length_a)
    fexp_nodes_b.append(exp_length_b)
    fexp_nodes_c.append(exp_length_c)
    fpath_lengths_c.append( path_length_c)
    
print(fpath_lengths_a,fpath_lengths_b)
plt.figure()
plt.plot(map_sizes, fpath_lengths_a)
plt.plot(map_sizes, fpath_lengths_b)
plt.plot(map_sizes, fpath_lengths_c)
plt.legend(['Best First', 'algorithm B', 'A*'])
plt.title('Path length vs map size')
plt.show()
plt.figure()
plt.plot(map_sizes, fexp_nodes_a)
plt.plot(map_sizes, fexp_nodes_b )
plt.plot(map_sizes, fexp_nodes_c )
plt.legend(['Best First', 'algorithm B','A*'])
plt.title('expended length vs map size')
plt.show()