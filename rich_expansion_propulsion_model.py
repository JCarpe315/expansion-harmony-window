# CC0 1.0 Universal Public Domain Dedication
# This work is dedicated to the public domain under CC0 1.0.

import numpy as np

class RichExpansionPropulsionModel:
    def __init__(self):
        self.state = {"q_factor": 8.0, "nozzle_field_T": 11.0, "thrust_vector": 1.0}
        self.dt = 0.1

    def _update_physics(self):
        coupling = (self.state["nozzle_field_T"] - 11.5) * (1.2 - abs(self.state["thrust_vector"] - 1.2))
        q_boost = 0.8 * coupling * 6.5
        self.state["q_factor"] += q_boost * self.dt

    def run(self, steps=800):
        for _ in range(steps):
            self._update_physics()
        print("Final Q:", round(self.state["q_factor"], 2))

if __name__ == "__main__":
    model = RichExpansionPropulsionModel()
    model.run()
