
class Energy:
    def __init__(self, color, capacity=0):
        self.unit = 30.5 * 10**3 # Defined by Joule
        self.capacity =  self.energy.energy // self.unit
        self.energy.energy = 0

        R, G, B = color
        self.R = R/255
        self.G = G/255
        self.B = B/255
        self.energySource = [self.R, self.G, self.B]


class Food:
    # R => protein
    # G => carbohydrate
    # B => fat
    def __init__(self, color, amount=amount):
        R, G, B = color
        nR, nG, nB = amount
        self.R = R/255
        self.G = G/255
        self.B = B/255
        self.capacity = [self.R, self.G, self.B]
        self.amount = [nR, nG, nB]
        self.color = color

    def consumeR(self)


class Waste:
    def __init__(self, color, amount):
        R, G, B = color
        self.R = R/255
        self.G = G/255
        self.B = B/255
        self.amount = [nR, nG, nB]

##########

def consumeE4G(sim, outEnergy): # photosynthesis
    if sim.energy.capacity > 18:
        sim.energy.capacity -= 18
        energy = sum(outEnergy.energySource) *.25
        sim.food = Food(color=(0, sim.waste.amount[1]*energy, 0))


def consumeG4B(sim): # acetylCoA to fatty acid
    nG = sim.waste.amount[1]
    if sim.energy.capacity > 7:
        sim.energy.capacity -= 7
        nB = nG *.5
        sim.food[2] = nB


def produceR(sim): # amino acid usage
    nR = sim.waste[0]
    if sim.energy.capacity > sum(nR)*2:
        sim.energy.capacity -= sum(nR)*2
        sim.food[0] = len(nR)

#############

def consumeFood(sim, food):
    if sim.energy.capacity > 4:
        sim.energy.capacity -= 4
        tmpR = food.capacity[0] * .20
        tmpG = food.capacity[1] * .30
        sim.energy.energy = tmpR + tmpG





def useEnergy2MovePerSec(sim, currentSpeed):
    # Mass defined by centimeters
    # Speed defined by meter per second => 1 meter is 3779pixel
    sim.energy -= 0.5*(sim.size*10**6, speed*(1/3779))

def useEnergy2Divide()
