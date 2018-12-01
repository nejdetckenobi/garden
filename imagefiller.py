from PIL import Image
from imps import Garden, Tree


class CustomTree(Tree):
    def __init__(self, *args, **kwargs):
        super(CustomTree, self).__init__(*args, **kwargs)

    def checked(self, p):
        in_image = super(CustomTree, self).checked(p)
        in_shape = self.garden.pxdata[p[0], p[1]][:3] == (255, 255, 255)
        return in_image and in_shape


class CustomGarden(Garden):
    def __init__(self, image, *args, **kwargs):
        super(CustomGarden, self).__init__(width=image.width,
                                           height=image.height)
        self.image = image
        self.pxdata = image.load()

    def add_tree(self, start_point, color):
        new_tree = CustomTree(start_point, color, self)
        self.trees.append(new_tree)


if __name__ == '__main__':
    fp = open('resources/eda.png', 'rb')
    img = Image.open(fp, mode='r')
    threshold = 127
    img2 = img.point(lambda p: p > threshold and 255)
    fp.close()

    cg = CustomGarden(img2)
    cg.add_tree((31, 81), (255, 0, 0))
    cg.add_tree((31, 141), (255, 255, 0))
    cg.add_tree((75, 105), (0, 0, 255))

    cg.add_tree((119, 69), (0, 0, 255))
    cg.add_tree((181, 107), (255, 255, 0))
    cg.add_tree((119, 144), (255, 0, 0))

    cg.add_tree((283, 129), (255, 0, 0))
    cg.add_tree((245, 71), (255, 255, 0))
    cg.add_tree((251, 121), (0, 0, 255))

    cg.make_gif('out.gif')
