from PIL import Image
import imageio
from io import BytesIO


class Garden(object):
    def __init__(self, width, height, memory):
        super(Garden, self).__init__()
        self.trees = []
        self.memory = memory
        self.width = width
        self.height = height

    def tick(self):
        for t in self.trees:
            if len(t.active):
                t.tick()

    def process(self):
        while sum([len(t.active) for t in self.trees]):
            self.tick()

    def dump(self):
        data = []
        for h in range(self.height):
            for w in range(self.width):
                data.append(self.memory.get((w, h), (0, 0, 0)))

        img = Image.new("RGB", (self.width, self.height), color=(0, 0, 0))
        img.putdata(data)
        return img

    def make_gif(self, filepath):
        with imageio.get_writer(filepath, mode="I", fps=60) as writer:
            while sum([len(t.active) for t in self.trees]):
                self.tick()
                temp = BytesIO()
                self.dump().save(temp, format="png")
                temp.seek(0)
                writer.append_data(imageio.imread(temp))
