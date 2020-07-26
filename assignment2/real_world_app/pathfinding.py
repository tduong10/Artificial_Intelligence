# Course:           CS4242
# Student name:     Timmy Duong
# Student ID:       000678536
# Assignment #:     2
# Due Date:         June 27
# Signature:           
# Score:  

"""
A* Search
    f(n) = g(n) + h(n)

    ** f(n) = evaluation function to select a node for expansion (usually the lowest code node)
    ** g(n) = cost from the initial state to the current state n
    ** h(n) = heuristic estimated cost of the cheapest path from node n to a goal node
"""

import random
import tkinter as tk
from tkinter import *
import numpy as np

row = 10
col = 10
gridSize = (row, col)
grid = np.random.randint(0, 3, size = gridSize) # random array between 0, 2
# if '0' then wall, else 1 or 2 is good to go through
# randrange(a, b+1)
end_x = random.randint(0, 9) # randomly choose a coord for x between 0 and 9
end_y = random.randint(0, 9) # randomly choose a coord for y between 0 and 9
grid[end_x][end_y] = 3 # '3' would be the end of the path

# starting point
start_x = random.randint(0, 9) # randrange(a, b+1)
start_y = random.randint(0, 9)
grid[start_x][start_y] = 4 # '4' is initial starting

master = tk.Tk()
master.title("A* Search")

class Node:
    def __init__(self, parent = None, node = None):
        self.parent = parent
        self.node = node
        self.f = 0
        self.g = 0
        self.h = 0
    
    """
    def __eq__(self, other):
        return self.node == other.node
    """

    def AstarSearch(grid, init_state, goal_state):
        open_set = []
        closed_set = []
        starting_node = Node(init_state, None)
        ending_node = Node(goal_state, None)
        open_set.append(starting_node)
        while (open_set != None):
            lowest_node = open_set[0]
            open_set.sort()
            lowest_node = open_set.pop(0) # pop first index
            closed_set.append(lowest_node)
            if (lowest_node == ending_node):
                mazepath = []
                while (lowest_node != None):
                    mazepath.append(lowest_node.node)
                    lowest_node = lowest_node.parent
                return mazepath[::-1]
            neighbors = []
            moves = [[0, -1],[0, 1], [-1, 0], [1, 0]]
            for location in moves:
                location_node = (lowest_node.node[0] + location_node.node[0], lowest_node.node[1] + lowest_node.node[1])
                neighbor_node = Node(lowest_node, location_node)
                neighbors.append(neighbor_node)
            for neighbor in neighbors:
                for node in closed_set:
                    if neighbor == node:
                        continue
                neighbor.g = lowest_node.g + neighbor.g
                neighbor.h = ((neighbor.node[0] - ending_node.node[0]) + (neighbor.node[1] - ending_node.node[1]))
                neighbor.f = neighbor.g + neighbor.h
                for chosen in open_set:
                    if (neighbor == chosen) and (chosen.f > neighbor.f):
                        return None
                    open_set.append(chosen)
            
class Pathfinder:      
    def Maze_Builder():
        maze = tk.Canvas(master, width = 500, height = 500, borderwidth = 1, relief = 'raised')
        maze.pack(side = "left")
        key = tk.Label(master, text = "Legend: \nGreen = Starting Point.\n Red = End Point.")
        key.pack(side = "bottom")

        for i in range(0, row):
            for j in range(0, col):
                if (grid[i][j] == 1 or grid[i][j] == 2):
                    maze.create_rectangle(i * 50, j * 50, (i + 1) * 50, (j + 1) * 50, fill = 'white')
                elif (grid[i][j] == 3):
                    maze.create_rectangle(i * 50, j * 50, (i + 1) * 50, (j + 1) * 50, fill = 'red')
                elif (grid[i][j] == 4):
                    maze.create_rectangle(i * 50, j * 50, (i + 1) * 50, (j + 1) * 50, fill = 'green')
                else:
                    maze.create_rectangle(i * 50, j * 50, (i + 1) * 50, (j + 1) * 50, fill = 'black')

        # calls the GUI
        master.mainloop()

# create object
#pf = Pathfinder(grid, init_x, init_y)
Pathfinder.Maze_Builder()
init_state = grid[start_x][start_y]
goal_state = grid[end_x][end_y]

search = Node.AstarSearch(grid, init_state, goal_state)
print(search)
#Pathfinder.Path_Finding(start_x, start_y)



