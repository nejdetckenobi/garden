#!/usr/bin/env python3

from imps import Garden


WIDTH = 100
HEIGHT = 100

# Sizes should be fit (2*k + 1) format. k is integer.
WIDTH = WIDTH + (WIDTH + 1) % 2
HEIGHT = HEIGHT + (HEIGHT + 1) % 2

# Output file name

if __name__ == '__main__':
    g = Garden(WIDTH, HEIGHT)
    g.add_tree((1, 1), (255, 0, 0))
    g.add_tree((WIDTH - 2, 1), (255, 255, 0))
    g.add_tree((1, HEIGHT - 2), (0, 255, 0))
    g.add_tree((WIDTH-2, HEIGHT-2), (0, 0, 255))
    g.add_tree((WIDTH // 2 - 1, HEIGHT // 2 - 1), (253, 89, 86))

    # Uncomment this line to make a GIF
    OUTPUT = 'lab.gif'
    g.make_gif(OUTPUT)
    
    # Uncomment these lines to get a PNG image
    #OUTPUT = 'lab.png'
    #g.process()
    #image = g.dump()
    #image.save(OUTPUT, format='png')
