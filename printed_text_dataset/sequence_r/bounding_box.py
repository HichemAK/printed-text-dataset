import numpy as np

class BoundingBox:
    def __init__(self, x: int, y: int, h: int, w: int):
        self.x = x
        self.y = y
        self.h = h
        self.w = w

    def slice(self, img):
        return img[self.x:self.w, self.y:self.h]