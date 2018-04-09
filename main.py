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
add_sphere(edges, 250, 250, 0, 100, 20)
add_spheret(polygons, 250, 250, 0, 100, 20)


draw_polygons(polygons, screen, color)
draw_lines(edges, screen, color)
display(screen)

