

ATPunit = 30.5 * 10**3

class Energy:
    def __init__(self):
        self.unit = ATPunit # Defined by Joule
        self.capacity = 0
        self. energy = 0

    def update_capacity(self, capacity):
        self.capacity += capacity
        self.energy.energy = self.capacity * self.unit


    def update_energy(self, energy):
        self.energy += energy
        self.capacity =  self.energy // self.unit



class Food:
    def __init__(self, size=32*32):
        self.size = size
        self.energy = size * 10**3
        food.capacity = self.energy // ATPunit


def consume_food(sim, food):
    sim.energy.update_capacity(food.capacity)

def consume_energy(sim, currentSpeed):
    tmpE = 0.5*(sim.size*10**6, speed*(1/3779))
    sim.energy.update_energy(tmpE)




    
