import math


def print_matrix( matrix ):
    elem_length = len(str(max(max(matrix)))) if len(matrix[0]) else 0
    for row in matrix:
        print '|',
        for element in row:
            print (' ' * (elem_length - len(str(element)))) + str(element),
        print '|'
    print ''

def ident( matrix ):
    # Take advantage of Python returning the last argument evaluated in a boolean expression
    matrix[:] = [[((row == col and 1) or 0) for col in xrange(len(matrix[row]))] for row in xrange(len(matrix))]
    

def scalar_mult( matrix, s ):
    matrix[:] = [[s * matrix[row][col] for col in xrange(len(matrix[row]))] for row in xrange(len(matrix))]

'''
a b c d   1  2  3  4  5
e f g h   6  7  8  9 10
i j k l  11 12 13 14 15
m n o p  16 17 18 19 20
'''

def tranpose(matrix):
    new_matrix = [[((row == col and matrix[row][col]) or matrix[col][row]) for col in xrange(len(matrix[row]))] for row in xrange(len(matrix))]
    return new_matrix
    
#m1 * m2 -> m2
def matrix_mult( m1, m2 ):
    m2_tranposed = tranpose(m2)

    for i in xrange(len(m1)):
        for j in xrange(len(m2_tranposed)):
            m2[i][j] = sum([(elem1 * elem2) for elem1, elem2 in zip(m1[i], m2_tranposed[j])])
                            
def new_matrix(rows = 4, cols = 4):
    m = []
    for c in range( cols ):
        m.append( [] )
        for r in range( rows ):
            m[c].append( 0 )
    return m

if __name__ == '__main__':
    a = [[1, 2, 3], [4, 5, 6]]
    print_matrix(a)
    scalar_mult(a, 4)
    print_matrix(a)
    ident(a)
    print_matrix(a)
    b = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    print_matrix(b)
    b = tranpose(b)
    print_matrix(b)
    ident(b)
    print_matrix(b)

    c = [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12], [13, 14, 15, 16]]
    d = [[1, 2, 3, 4], [2, 3, 4, 5], [3, 4, 5, 6], [4, 5, 6,7]]

    print_matrix(c)
    print_matrix(d)
    matrix_mult(c, d)
    print_matrix(d)
