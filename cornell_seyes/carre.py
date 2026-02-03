
from reportlab.platypus import Flowable
from reportlab.lib import colors
from reportlab.lib.units import mm, toLength


class CarreBlock(Flowable):
    def __init__(self, width, height, line_gap=5 * mm):
        super().__init__()
        self.width = float(width)
        self.height = float(height)
        self.line_gap = float(line_gap)

    def wrap(self, availWidth, availHeight):
        return self.width, self.height - 10

    def draw(self):
        c = self.canv
        y = 0.0
        c.setStrokeColor(colors.lightblue)
        c.setLineWidth(0.3)
        while y <= self.height - 3:    
            c.line(0, y, self.width - 10, y)
            y += self.line_gap

        x = 0.0
        while x <= self.width - 3:
            c.line(x, 0, x, self.height - 10)
            x += self.line_gap
