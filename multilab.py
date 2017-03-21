from PIL import Image
from random import choice, randrange
from argparse import ArgumentParser


parser = ArgumentParser()
parser.add_argument('WIDTH', type=int)
parser.add_argument('HEIGHT', type=int)
parser.add_argument('OUTPUT', type=str)
# parser.add_argument('--colors', type=list, nargs='*')
args = parser.parse_args()
WIDTH = args.WIDTH + (args.WIDTH + 1) % 2
HEIGHT = args.HEIGHT + (args.HEIGHT + 1) % 2
OUTPUT = args.OUTPUT
# COLORS = args.colors if args.colors else ['#FFF']


def checked(p):
    return 0 < p[0] < WIDTH and 0 < p[1] < HEIGHT


def mid_point(p1, p2):
    return (p1[0]+p2[0])/2, (p1[1]+p2[1])/2


class Tree(object):
    def __init__(self, start_point, color):
        super(Tree, self).__init__()
        self.start_point = start_point
        self.color = color
        self.current_point = start_point
        self.active = [self.current_point]
        self.visited = {}
        self.mapper = {}

    def tick(self):
        left = (self.current_point[0] - 2, self.current_point[1])
        right = (self.current_point[0] + 2, self.current_point[1])
        up = (self.current_point[0], self.current_point[1] + 2)
        down = (self.current_point[0], self.current_point[1] - 2)

        neighbours = [n for n in (left, right, up, down)
                      if checked(n) and n not in self.visited]

        if not neighbours:
            index = randrange(0, len(self.active))
            self.current_point = self.active[index]
            self.active.pop(index)
        else:
            picked = choice(neighbours)
            self.visited[picked] = 1
            self.active.append(picked)
            m = mid_point(self.current_point, picked)
            self.mapper[m] = self.color
            self.mapper[self.current_point] = self.color
            self.mapper[picked] = self.color
            self.current_point = picked


class Garden(object):
    def __init__(self, width, height):
        super(Garden, self).__init__()
        self.trees = []
        self.mapper = {}
        self.visited = {}
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
        data = []
        for h in range(self.height):
            for w in range(self.width):
                data.append(self.mapper.get((w, h), (0, 0, 0)))

        img = Image.new('RGB', (self.width, self.height), color=(0, 0, 0))
        img.putdata(data)
        img.save(filepath, format='png')


if __name__ == '__main__':
    g = Garden(WIDTH, HEIGHT)
    g.add_tree((1, 1), (255, 0, 0))
    g.add_tree((WIDTH - 2, 1), (255, 255, 0))
    g.add_tree((1, HEIGHT - 2), (0, 255, 0))
    g.add_tree((WIDTH-2, HEIGHT-2), (0, 0, 255))
    g.process()
    g.dump(OUTPUT)
