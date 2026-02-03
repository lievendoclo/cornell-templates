
from reportlab.platypus import Flowable
from reportlab.lib import colors

class SeyesBlock(Flowable):
    def __init__(self, width, height, line_gap=6.1):
        super().__init__()
        self.width = float(width)
        self.height = float(height)
        self.line_gap = float(line_gap)

    def wrap(self, availWidth, availHeight):
        return self.width, self.height - 10

    def draw(self):
        c = self.canv
        y = 0.0
        counter = 0
        while y <= self.height - 3:
            c.setStrokeColor(colors.lightblue)
            if counter % 4 == 0:
                c.setLineWidth(0.5)
            else:
                c.setLineWidth(0.3)
            c.line(0, y, self.width - 10, y)
            counter += 1
            y += self.line_gap

