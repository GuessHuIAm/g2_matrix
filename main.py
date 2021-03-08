import random
from display import *
from draw import *
from matrix import *

print('Testing add_edge. Adding (1, 2, 3), (4, 5, 6) m2 = ')
m2 = new_matrix(rows=4, cols=0)
add_edge(m2, 1, 2, 3, 4, 5, 6)
print_matrix(m2)
print('\n')

print('Testing ident. m1 = ')
m1 = new_matrix()
ident(m1)
print_matrix(m1)
print('\n')

print('Testing matrix mult. m1 * m2 = ')
matrix_mult(m1, m2)
print_matrix(m2)
print('\n')

print('Testing matrix mult. m3 = ')
m3 = new_matrix(rows = 4, cols = 0)
add_point(m3, 10, 10, 10)
add_point(m3, 30, 60, 90)
add_edge(m3, 15, 30, 45, 60, 75, 90)
print_matrix(m3)
print('\n')

print('Testing matrix mult. m4 = ')
m4 = new_matrix(rows = 4, cols = 0)
add_point(m4, 0, 45, 90)
add_point(m4, 45, 90, 0)
add_point(m4, 90, 45, 0)
print_matrix(m4)
print('\n')

print('Testing matrix mult. m3 * m4 = ')
matrix_mult(m3, m4)
print_matrix(m4)
print('\n')

def r():
    return random.randint(-25, 25)

screen = new_screen()
d = 0
e = 10

for i in range(3):
    x = XRES
    y = YRES
    d += 25
    e += 5

    color = [191 + r(), 230 + r(), 255]
    tri1 = new_matrix()

    for x in range(x - (2 * e)):
        add_edge(tri1, x + e, y - e, 0, d, d, 0)
        y -= 1
    draw_lines(tri1, screen, color)

    color = [144 + r(), 230 + r(), 144 + r()]
    tri2 = new_matrix()
    y = YRES
    d += 25
    e += 5

    for x in range(x - (2 * e)):
        add_edge(tri2, XRES - x - e, y - e, 0, d, YRES - d, 0)
        y -= 1
    draw_lines(tri2, screen, color)

    color = [255, 204 + r(), 203 + r()]
    tri3 = new_matrix()
    y = YRES
    d += 25
    e += 5

    for x in range(x - (2 * e)):
        add_edge(tri3, x + e, y - e, 0, XRES - d, YRES - d, 0)
        y -= 1
    draw_lines(tri3, screen, color)

    color = [255, 252, 187 + r()]
    tri4 = new_matrix()
    y = YRES
    d += 25
    e += 5

    for x in range(x - (2 * e)):
        add_edge(tri4, XRES - x - e, y - e, 0, XRES - d, d, 0)
        y -= 1
        draw_lines(tri4, screen, color)

save_ppm_ascii(screen, 'pic.ppm')
save_extension(screen, 'spiral.png')
display(screen)
