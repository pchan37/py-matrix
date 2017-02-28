from __future__ import division

from display import *
from draw import *

from math import floor, pi, cos, sin
from random import randrange

screen = new_screen()
color = [ 0, 255, 0 ]
matrix = new_matrix(0, 4)

# CONSTANTS Used for drawing spokes of a circle
SECTIONS = 32
INTERVAL = pi / SECTIONS * 2

# CONSTANTS specifying the range of random numbers to populate the test matrix
START = 20
END = 60

# CONSTANTS specifying the interval to generate the scalar to multiply test matrix by
SCALAR_START = 0
SCALAR_END = 5

print_matrix(matrix)

def dy(theta):
    return sin(INTERVAL * theta)

def dx(theta):
    return cos(INTERVAL * theta)

print 'Using add_edge...'
for i in xrange(SECTIONS):
    x0 = 250
    y0 = 250
    z0 = 0
    x1 = 250 + int(250 * dx(i))
    y1 = 250 + int(250 * dy(i))
    z1 = 0
    add_edge(matrix, x0, y0, z0, x1, y1, z1)

print 'Resulting matrix'
print_matrix(matrix)

def populate(matrix):
    for row in xrange(len(matrix)):
        for col in xrange(len(matrix[0])):
            matrix[row][col] = randrange(START, END)

testMatrix = new_matrix()
populate(testMatrix)

c = new_matrix()
d = new_matrix()
populate(c)
populate(d)

print "Testing scalar multiplication"
print_matrix(testMatrix)
scalar = randrange(SCALAR_START, SCALAR_END)
print "Multiplying matrix by: " + str(scalar)
scalar_mult(testMatrix, scalar)
print_matrix(testMatrix)

print "Testing identity matrix generation"
print_matrix(testMatrix)
ident(testMatrix)
print_matrix(testMatrix)

print "Testing matrix multiplication"
print_matrix(c)
print_matrix(d)
matrix_mult(c, d)
print_matrix(d)

draw_lines( matrix, screen, color )
display(screen)
