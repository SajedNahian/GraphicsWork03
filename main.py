from display import *
from draw import *
from scriptParser import *
from matrix import *
from random import randint

screen = new_screen()
color = [ 0, 255, 0 ]
edges = []
transform = new_matrix()

parse_file( 'script', edges, transform, screen, color )