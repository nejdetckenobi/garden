from random import choice, randrange


def mid_point(p1, p2):
    return (p1[0]+p2[0])/2, (p1[1]+p2[1])/2


class Tree(object):
    def __init__(self, start_point, color, garden):
        super(Tree, self).__init__()
        self.garden = garden
        self.start_point = start_point
        self.color = color
        start_point = (2 * (start_point[0] // 2) + 1,
                       2 * (start_point[1] // 2) + 1)
        self.current_point = start_point
        self.active = [self.current_point]
        if self.current_point in self.garden.mapper:
            raise ValueError('Your starting point conflicts '
                             'with at least one of existing Tree objects\'')
        self.garden.mapper[self.current_point] = self.color

    def checked(self, p):
        return 0 < p[0] < self.garden.width and 0 < p[1] < self.garden.height

    def tick(self):
        left = (self.current_point[0] - 2, self.current_point[1])
        right = (self.current_point[0] + 2, self.current_point[1])
        up = (self.current_point[0], self.current_point[1] + 2)
        down = (self.current_point[0], self.current_point[1] - 2)

        neighbours = [n for n in (left, right, up, down)
                      if self.checked(n) and n not in self.garden.mapper]

        if not neighbours:
            index = randrange(0, len(self.active))
            self.current_point = self.active[index]
            self.active.pop(index)
        else:
            picked = choice(neighbours)
            self.active.append(picked)
            m = mid_point(self.current_point, picked)
            self.garden.mapper[m] = self.color
            self.garden.mapper[self.current_point] = self.color
            self.garden.mapper[picked] = self.color
            self.current_point = picked
