# Author: Xiaoxuan
# Date: 6/3/2021
# Purpose: implement Dartmouth pathfinder with names of start and goal
from cs1lib import *
from load_graph import load_graph
from bfs import bfs
WIN_WIDTH = 1012
WIN_HEIGHT = 811
# mouse state
mpressed = False
mx = None
my = None
# start vertex and goal vertex
start = None
goal = None


# capture mouth movement
def my_mmove(x, y):
    global mx, my
    mx = x
    my = y


# change state of mpressed
def my_mpress(mx, my):
    global  mpressed
    mpressed = True


# change state of mpressed
def my_mrelease(mx, my):
    global  mpressed
    mpressed = False


# main draw function
def main_draw():
    global start, goal

    draw_image(img, 0, 0)

    for key in vdict:
        vertex = vdict[key]

        # draw vertices and edges in blue
        vertex.draw_vertex(0, 0, 1)
        vertex.draw_edges(0, 0, 1)

        # capture start and goal
        if vertex.on_vertex(mx, my):
            if mpressed:
                start = vertex
            else:
                goal = vertex

    if start and goal:
        path = bfs(start, goal)
        if path:
            # draw path in red
            for i in range(len(path)-1):
                path[i].draw_vertex(1, 0, 0)
                path[i].connect(path[i+1], 1, 0, 0)
            path[-1].draw_vertex(1, 0, 0)
            # display names of start and goal in pink
            start.display_name(1, 0, 1)
            goal.display_name(1, 0, 1)


img = load_image('dartmouth_map.png')
vdict = load_graph('dartmouth_graph.txt')

start_graphics(main_draw, width=WIN_WIDTH, height=WIN_HEIGHT, mouse_move=my_mmove, mouse_press=my_mpress, mouse_release=my_mrelease)
