import random


class Neuron():
    def __init__(self, x,y, potential = 0,charge_rate = 0.1,threshold = 10, potential_reset = 0, reset_randomness = 0, fire_power = 1):
        self.x = x
        self.y = y
        self.potential = potential
        self.axons = []
        self.dendrites = []
        self.threshold = threshold
        self.potential_reset = potential_reset
        self.reset_randomness = reset_randomness
        self.charge_rate = charge_rate
        self.fire_power = fire_power
        self.is_fireing = False

    def addAxon(self, axon):
        self.axons.append(axon)

    def add_potential(self, charge):
        self.potential += charge
    
    def get_x(self):
        return self.x
    def get_y(self):
        return self.y
    def get_coords(self):
        return self.x, self.y
    def get_fire_power(self):
        return self.fire_power
    
    def addDendrite(self, dendrite):
        self.dendrites.append(dendrite)

    def fire(self):
        if self.potential >= self.threshold:
            for axon in self.axons:
                axon.fire()
            self.potential = self.potential_reset + random.uniform(-self.reset_randomness, self.reset_randomness)
            self.is_fireing = True

    def unfire(self):
        self.is_fireing = False