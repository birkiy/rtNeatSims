

from random import gauss

class simGenome:
    sim = Network()
    def __init__(self, sim):
        self.id = sim.id
        self.fitness = None

    def mutate(self, config):

        if gauss(5*10**-8, 10**-10) < config.node_add_prob:
            sim.add_node(simGene)
        # if random() < config.egde_remove_prob:
        #     sim.remove_node(self)
        if gauss(5*10**-8, 10**-10) < config.edge_add_prob:
            sim.add_edge()

        if gauss(5*10**-8, 10**-10) < config.edge_disable_prob:
            sim.disable_edge()

        # for node in sim.nodes:

    def size(self):
        num_enabled_connections = sum([1 for cg in self.edges.values() if cg.enabled])
        return len(self.nodes), num_enabled_connections


    def add_connection(self, input_key, output_key, weight, enabled):
        key = (input_key, output_key)
        connection = simConnection(key)
        connection.weight = weight
        connection.enabled = enabled
        self.edges[key] = connection



class simConnection:
    def __init__(self, key):
        self.key = key
        connection.weight = None
        connection.enabled = None

class configGenome:
    def __init__(self):
        self.node_add_prob = 10**-8
        self.edge_add_prob = 10**-8
        self.edge_disable_prob = 10**-7


class simGene:
    def __init__(self, key):
        self.key = key
        self.activation_function = ActivationFunctionSet[randint(len(ActivationFunctionSet)+1)]
        self.activation_function = AggregationFunctionSet[randint(len(AggregationFunctionSet)+1)]
        self.value = 0
        self.min_value = 0
        self.max_value = 1
        self.innovation = key

    def clamp(self, value):
        min_value = self.min_value
        max_value = self.max_value
        return max(min(value, max_value), min_value)

    def mutate(self):
        v = self.value

        mutate_rate = 10**-7

        r = gauss(5*10**-8, 10**-10)
        if r < mutate_rate:
            mutate_power = 0.5
            v = self.clamp(v + gauss(0.0, mutate_power))

        setattr(self, "value", v)
