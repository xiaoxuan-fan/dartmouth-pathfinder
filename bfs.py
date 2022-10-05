# Author: Xiaoxuan
# Date: 6/3/2021
# Purpose: breadth-first search (input start and goal vertices, output a path with fewest edges)
from collections import deque


def bfs(start, goal):
    frontier = deque()
    backpointer = {}

    frontier.append(start)
    backpointer[start] = None

    while frontier:
        curr_v = frontier.popleft()
        for neighbour in curr_v.adj_list:
            if neighbour not in backpointer:  # if unvisited
                frontier.append(neighbour)
                backpointer[neighbour] = curr_v
        # if goal is found, assemble a list of vertices on the path
        if goal in backpointer:
            path = []
            curr_v = goal
            while curr_v:
                path.append(curr_v)
                curr_v = backpointer[curr_v]
            return path
