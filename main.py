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
add_boxt(polygons, 250, 250, 0, 100, 100, 100)
ident(transform)
matrix_mult(make_rotX(45), transform)
matrix_mult(make_rotY(45), transform)
matrix_mult(transform, polygons)

draw_polygons(polygons, screen, color)
display(screen)
