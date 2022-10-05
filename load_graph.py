# Author: Xiaoxuan
# Date: 5/31/2021
# Purpose: build a dictionary of vertices from data file
from vertex import Vertex


def load_graph(fname):
    vdict = {}

    # create vertex objects with name and coordinates and add to dictionary
    fp = open(fname, 'r')
    for line in fp:
        info = line.split(';')
        name = info[0].strip()
        coordinates = info[2].split(',')
        x = int(coordinates[0])
        y = int(coordinates[1])
        vdict[name] = Vertex(name, x, y)
    fp.close()

    # fill in adjacency list in each vertex object
    fp = open(fname, 'r')
    for line in fp:
        info = line.split(';')
        name = info[0].strip()
        neighbours = info[1].split(',')
        for neighbour in neighbours:
            vdict[name].adj_list.append(vdict[neighbour.strip()])
    fp.close()

    return vdict
