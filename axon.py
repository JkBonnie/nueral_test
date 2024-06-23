import math

class Axon:
    def __init__(self, neuron, direction, length=0.5):
        self.neuron = neuron
        self.endpoint_x = self.neuron.get_x() + math.cos(math.radians(direction)) * length
        self.endpoint_y = self.neuron.get_y() + math.sin(math.radians(direction)) * length
        
    def find_in_range_dendrites(self, all_dendrites):
        fire_power = self.neuron.get_fire_power()
        self.dendrites_in_range = []
        self.dendrites_in_range_fp = []

        for dendrite in all_dendrites: #loop through dendrites and add charge to the dendrties in range in range
            x_distance = abs(dendrite.get_x() - self.endpoint_x)
            y_distance = abs(dendrite.get_y() - self.endpoint_y)
            #adds charge for x if in range
            if dendrite.get_range() - math.sqrt(x_distance**2+y_distance**2) > 0: # only adds charge if in range
                #adds charge for x if in range
                normalized_dist = x_distance/dendrite.get_range()
                fire_percent = normalized_dist**dendrite.get_rangefalloff()
                dendrite_fire_adj_X = fire_power*fire_percent
            
                #adds charge for y if in range
            
                normalized_dist = y_distance/dendrite.get_range()
                fire_percent = normalized_dist**dendrite.get_rangefalloff()
                dendrite_fire_adj_Y = (fire_power*fire_percent)
                #adds charge to dendrite
                dendrite_recieved_fire = math.sqrt(dendrite_fire_adj_X**2 + dendrite_fire_adj_Y**2)
                #adds dendrite to list of dendrites in range as well as the amount of charge it recieved
                self.dendrites_in_range.append(dendrite)
                self.dendrites_in_range_fp.append(dendrite_recieved_fire)


    def fire(self):
        for i in range(len(self.dendrites_in_range)):
            self.dendrites_in_range[i].add_charge(self.dendrites_in_range_fp[i])

    def get_neuron(self):
        return self.neuron

    def set_neuron(self, neuron):
        self.neuron = neuron