from neuron import Neuron
from axon import Axon
from dendrite import Dendrite

def main():
    axons = []
    dendrites = []
    neuron = Neuron(0,0)
    axon = Axon(neuron, 180, 1)
    neuron.addAxon(axon)
    axons.append(axon)
    dendrite = Dendrite(neuron, 0)
    neuron.addDendrite(dendrite)
    dendrites.append(dendrite)
    axon.find_in_range_dendrites(dendrites)
    

    neuron2 = Neuron(-2.5,0, potential = 10,charge_rate = 0.1,threshold = 10, potential_reset = 0, reset_randomness = 0, fire_power = 1)
    axon2 = Axon(neuron2, 0, 2)
    neuron2.addAxon(axon2)
    axons.append(axon2)
    dendrite2 = Dendrite(neuron2, 0)
    neuron2.addDendrite(dendrite2)
    dendrites.append(dendrite2)

    axon.find_in_range_dendrites(dendrites)
    axon2.find_in_range_dendrites(dendrites)
    neuron2.fire()
    dendrite.transmit_charge()
    dendrite2.transmit_charge()





#     print(dendrite.charge)
    print("neuron1 potential: ", neuron.potential)
    print("neuron2 potential: ", neuron2.potential)
    print("dendrite1 charge: ", dendrite.charge)
    print("dendrite2 charge: ", dendrite2.charge)

#     print(neuron.potential_reset)
#     print(neuron.reset_randomness)
#     print(neuron.threshold)
#     print(neuron.charge_rate)
#     print(neuron.fire_power)
#     print(neuron.x)
#     print(neuron.y)
#     print(neuron.axons)
#     print(neuron.dendrites)
#     print(axon.neuron)
#     print(axon.direction)
#     print(axon.length)
#     print(axon.endpoint_x)
#     print(axon.endpoint_y)
#     print(axon.dendrites_in_range)
#     print(axon.dendrites_in_range_fp)
#     print(dendrite.neuron)
#     print(dendrite.charge)
#     print(dendrite.range)
#     print(dendrite.range_falloff)
#     print(dendrite.output)
#     print(neuron.get_x())
#     print(neuron.get_y())
#     print(neuron.get_fire_power())
#     print(neuron.potential)
#     print(neuron.threshold)
#     print(neuron.potential_reset)
#     print(neuron.reset_randomness)
#     print(neuron.charge_rate)
#     print(neuron.fire_power)
#     print(neuron.axons)
#     print(neuron.dendrites)
#     print(axon.neuron)
#     print(axon.direction)
#     print(axon.length)
#     print(axon.endpoint_x)
#     print(axon.endpoint_y)
#     print(axon.dendrites_in_range)
#     print(axon.dendrites_in_range_fp)
#     print(dendrite.neuron)
#     print(dendrite.charge)
#     print(dendrite.range)
#     print(dendrite.range_falloff)
#     print(dendrite.output)
#     print(neuron.get_x())
#     print(neuron.get_y())
#     print(neuron.get_fire_power())
#     print(neuron.potential)
#     print(neuron.threshold)
#     print(neuron.potential_reset)
#     print(neuron.reset_randomness)
#     print(neuron.charge_rate)

main()