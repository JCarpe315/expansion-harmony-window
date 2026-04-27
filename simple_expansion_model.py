# CC0 1.0 Universal Public Domain Dedication
# This work is dedicated to the public domain under CC0 1.0.

import numpy as np

class SimpleExpansionModel:
    def __init__(self):
        self.q = 8.0
        self.nozzle = 11.0

    def step(self):
        self.q += 0.5 * (self.nozzle - 11.5)
        print("Q:", round(self.q, 2))

if __name__ == "__main__":
    model = SimpleExpansionModel()
    for _ in range(10):
        model.step()
