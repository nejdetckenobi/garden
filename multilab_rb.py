from PIL import Image
import numpy
from random import choice
from collections import defaultdict
from argparse import ArgumentParser


parser = ArgumentParser()
parser.add_argument('WIDTH', type=int)
parser.add_argument('HEIGHT', type=int)
parser.add_argument('OUTPUT', type=str)

args = parser.parse_args()
WIDTH = args.WIDTH + (args.WIDTH + 1) % 2
HEIGHT = args.HEIGHT + (args.HEIGHT + 1) % 2
OUTPUT = args.OUTPUT


def checked(p):
    return 0 < p[0] < WIDTH and 0 < p[1] < HEIGHT


def mid_point(p1, p2):
    return (p1[0]+p2[0])//2, (p1[1]+p2[1])//2


class Tree(object):
    def __init__(self, start_point, color):
        super(Tree, self).__init__()
        self.start_point = start_point
        self.color = color
        self.current_point = start_point
        self.active = [self.current_point]
        self.visited = defaultdict(int)
        self.visited[self.current_point] = 1
        self.mapper = {}

    def tick(self):
        left = (self.current_point[0] - 2, self.current_point[1])
        right = (self.current_point[0] + 2, self.current_point[1])
        up = (self.current_point[0], self.current_point[1] + 2)
        down = (self.current_point[0], self.current_point[1] - 2)

        neighbours = [n for n in (left, right, up, down)
                      if checked(n) and not self.visited[n]]

        if not neighbours:
            # Recursive Backtracker
            self.current_point = self.active.pop()
            # Prim's below. Slower but lesser bias.
            # index = randrange(0, len(self.active))
            # self.current_point = self.active[index]
            # self.active.pop(index)
        else:
            picked = choice(neighbours)
            self.visited[picked] = 1
            self.active.append(picked)
            m = mid_point(self.current_point, picked)
            self.mapper[m[1], m[0]] = self.color
            self.mapper[self.current_point[1], self.current_point[0]] = self.color
            self.mapper[picked[1], picked[0]] = self.color
            self.current_point = picked


class Garden(object):
    def __init__(self, width, height):
        super(Garden, self).__init__()
        self.trees = []
        self.mapper = numpy.zeros((height, width, 3), 'uint8')
        self.visited = defaultdict(int)
        self.width = width
        self.height = height

    def tick(self):
        for t in self.trees:
            t.tick()

    def add_tree(self, start_point, color):
        new_tree = Tree(start_point, color)
        new_tree.mapper = self.mapper
        new_tree.visited = self.visited
        self.trees.append(new_tree)

    def process(self):
        while sum([len(t.active) for t in self.trees]):
            for t in self.trees:
                if len(t.active):
                    t.tick()

    def dump(self, filepath):
        img = Image.fromarray(self.mapper,
                              mode='RGB')

        img.save(filepath, format='png')


if __name__ == '__main__':
    g = Garden(WIDTH, HEIGHT)
    g.add_tree((1, 1), [255, 0, 0])
    g.add_tree((WIDTH - 2, 1), [255, 255, 0])
    g.add_tree((1, HEIGHT - 2), [0, 255, 0])
    g.add_tree((WIDTH-2, HEIGHT-2), [0, 0, 255])
    g.add_tree(((WIDTH - 1) // 2 + 1 + ((WIDTH - 1) // 2) % 2,
                (HEIGHT - 1) // 2 + 1 + ((HEIGHT - 1) // 2) % 2),
               (0, 127, 255))
    g.process()
    g.dump(OUTPUT)
