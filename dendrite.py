import math

class Dendrite():
    def __init__(self,neuron,direction,charge = 0, length=0.05, range =1, range_falloff_power = 2):
        self.neuron = neuron
        self.charge = charge
        self.range = range
        self.range_falloff = range_falloff_power
        self.output = 0
        self.endpoint_x = self.neuron.get_x() + math.cos(math.radians(direction)) * length
        self.endpoint_y = self.neuron.get_y() + math.sin(math.radians(direction)) * length

    def transmit_charge(self):
        self.neuron.add_potential(self.charge)
        self.charge = 0

    def add_charge(self, charge):
        self.charge += charge

    def get_rangefalloff(self):
        return self.range_falloff

    def get_range(self):
        return self.range
    
    def get_x(self):
        return self.endpoint_x
    
    def get_end_coords(self):
        return self.endpoint_x, self.endpoint_y
    
    def get_start_coords(self):
        return self.neuron.get_coords()
    
    def get_y(self):
        return self.endpoint_y
    
    def get_neuron(self):
        return self.neuron

    def set_neuron(self, neuron):
        self.neuron = neuron
