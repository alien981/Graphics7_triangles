from display import *
from draw import *
from parser import *
from matrix import *
import math

screen = new_screen()
color = [ 0, 255, 0 ]
edges = []
transform = new_matrix()
polygons = []

# print_matrix( make_bezier() )
# print
# print_matrix( make_hermite() )
# print

#parse_file( 'script', edges, transform, screen, color )
clear_screen(screen)
add_polygon(polygons, 0, 0, 0, 0, 250, 0, 250, 0, 0)
draw_polygons(polygons, screen, color)
display(screen)
