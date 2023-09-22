# My first GUI
# Program: Print a tree with stars

image = [
    [0,0,0,0,0,1,0,0,0,0,0],
    [0,0,0,0,1,1,1,0,0,0,0],
    [0,0,0,1,1,1,1,1,0,0,0],
    [0,0,1,1,1,1,1,1,1,0,0],
    [0,1,1,1,1,1,1,1,1,1,0],
    [0,0,0,0,0,1,0,0,0,0,0],
    [0,0,0,0,0,1,0,0,0,0,0],
]

# 1. if pixel is 1 -> print *
# 2. if pixel is 0 -> print a space (' ')

for row in image: # iterates row
    for pixel in row: # iterates pixel in each row
        if pixel == 1:
            print('*', end='')
        else:
            print(' ', end='')
    print('')