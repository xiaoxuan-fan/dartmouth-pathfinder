# Author: Xiaoxuan
# Date: 6/3/2021
# Purpose: create a vertex class to represent places on dartmouth campus
from cs1lib import *
VERTEX_RADIUS = 5
EDGE_WIDTH = 2
FONT_SIZE = 15


class Vertex:
    def __init__(self, name, x, y):
        self.name = name
        self.x = x
        self.y = y
        self.adj_list = []

    # draw self
    def draw_vertex(self, r, g, b):
        disable_stroke()
        set_fill_color(r, g, b)
        draw_circle(self.x, self.y, VERTEX_RADIUS)

    # draw an edge between self and another vertex
    def connect(self, neighbour, r, g, b):
        enable_stroke()
        set_stroke_color(r, g, b)
        set_stroke_width(EDGE_WIDTH)
        draw_line(self.x, self.y, neighbour.x, neighbour.y)

    # draw edges between self and all neighbours
    def draw_edges(self, r, g, b):
        for neighbour in self.adj_list:
            self.connect(neighbour, r, g, b)

    # check if given location is on self
    def on_vertex(self, x, y):
        if x and y:
            return self.x - VERTEX_RADIUS <= x <= self.x + VERTEX_RADIUS and self.y - VERTEX_RADIUS <= y <= self.y + VERTEX_RADIUS

    # display the name of the vertex
    def display_name(self, r, g, b):
        enable_stroke()
        set_stroke_color(r, g, b)
        set_font_size(FONT_SIZE)
        draw_text(self.name, self.x, self.y)

    # def __str__(self):
    #     mystr = self.name + '; Location: ' + str(self.x) + ', ' + str(self.y) + '; Adjacent vertices: '
    #     for i in range(len(self.adj_list)-1):
    #         mystr += self.adj_list[i].name + ', '
    #     mystr += self.adj_list[-1].name
    #     return mystr
