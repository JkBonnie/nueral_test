import pygame
import sys
from axon import Axon
from neuron import Neuron
from dendrite import Dendrite

class Simulation_display():

    def __init__(self, window_x, window_y, neurons, axons, dendrites):
        # Initialize pygame
        pygame.init()
        self.window_x = window_x
        self.window_y = window_y
        self.window = window_x, window_y
        self.neurons: list[Neuron] = neurons
        self.axons: list[Axon] = axons
        self.dendrites: list[Dendrite] = dendrites
    

        # Set up the display
        self.window = pygame.display.set_mode((self.window_x, self.window_y))
        pygame.display.set_caption("Neural Network Visualization")

        # Colors
        self.BLACK = (0, 0, 0)
        self.WHITE = (255, 255, 255)
        self.RED = (255, 0, 0)
        self.GREEN = (0, 255, 0)
        self.YELLOW = (255, 255, 0)
        self.PINK = (255, 0, 255)

    def draw(self):
        # Clear the screen
        self.window.fill(self.WHITE)

        # Draw axons if firing, yellow, else pink
        for axon in self.axons:
            if axon.is_fireing:
                pygame.draw.line(surface = self.window,
                                 color = self.YELLOW,
                                 start_pos=axon.get_startpoint(),
                                 end_pos=axon.get_endpoint(), width=2)
            else:
                pygame.draw.line(surface = self.window,
                                color = self.PINK,
                                start_pos=axon.get_startpoint(),
                                end_pos=axon.get_endpoint(), width=2)


        # Draw dendrites
        for dendrite in self.dendrites:
            pygame.draw.line(surface=self.window, color=self.GREEN, start_pos=dendrite.get_start_coords(), end_pos=dendrite.get_end_coords(), width=2)
        
        # Draw neurons (if fireing, red, else black)
        for neuron in self.neurons:
            if neuron.is_fireing:
                pygame.draw.circle(surface=self.window, color=self.RED, center=neuron.get_coords(), radius=10)
            else:
                pygame.draw.circle(surface=self.window, color=self.BLACK, center =neuron.get_coords(), radius = 10)
        # Update the displaydisplay
        pygame.display.flip()

    def run(self):
        # Main loop
        running = True
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    # Exit the loop when a mouse button is clicked
                    running = False
            self.draw()
        self.quit()
        
    # Quit pygame
    def quit():
        pygame.quit()
        sys.exit()
