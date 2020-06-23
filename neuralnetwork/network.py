from random import randint, uniform

from neuralnetwork.edge import Edge
from neuralnetwork.node import Node
from neuralnetwork.id import Id


class Network:
    def __init__(self, input, output):
        self.nodes = []
        self.id = Id()
        self.nodes += [Node(self.id.id(), -1) for _ in range(input)]
        self.nodes += [Node(self.id.id(), 1) for _ in range(output)]
        self.nodedict = {node.id: node for node in self.nodes}
        self.edges = {}


    def __check_loop(self, node, visited, recursed):
        visited[node.id] = True
        recursed[node.id] = True

        for key, edge in self.edges.items():
            if key[1] == node.id:
                if not edge.disabled:
                    if not visited[node.id]:
                        if self.__check_loop(edge.begin, visited, recursed):
                            return True
                    elif recursed[edge.begin]:
                        return True

        recursed[node.id] = False
        return False


    def check_loop(self):
        visited = {node.id: False for node in self.nodes}
        recursed = {node.id: False for node in self.nodes}
        for node in self.nodes:
            if not visited[node.id]:
                if self.__check_loop(node, visited, recursed):
                    return True

        return False


    def add_edge(self):
        begin = self.nodes[randint(0, len(self.nodes)-1)]
        end = self.nodes[randint(0, len(self.nodes)-1)]
        'or (begin.id, end.id) in self.edges'
        while end.type < 1 or begin.type > -1:
            begin = self.nodes[randint(0, len(self.nodes)-1)]
            end = self.nodes[randint(0, len(self.nodes)-1)]

        self.edges[(begin.id, end.id)] = Edge(begin.id, end.id)
        while self.check_loop():
            self.edges[(begin.id, end.id)] = Edge(begin.id, end.id)


    def add_node(self):
        if len(self.edges):
            key, edge = list(self.edges.items())[randint(0, len(self.edges.values())-1)]
            del self.edges[key]
            id = self.id.id()

            edge1 = edge.copy_with_end(id)
            edge2 = edge.copy_with_begin(id)
            self.edges[edge1.begin, edge1.end] = edge1
            self.edges[edge2.begin, edge2.end] = edge2
            self.nodes += [Node(id, 0)]
            self.nodedict[id] = self.nodes[-1]


    def change_edge(self):
        if len(self.edges):
            edge = list(self.edges.values())[randint(0, len(self.edges.values())-1)]
            edge.weight = uniform(0, 1)

    def __str__(self):
        s = ''
        s += f'Nodes: ({len(self.nodes)})\n'
        for node in self.nodes:
            s += str(node)
        s += f'\nEdges: ({len(self.edges)})\n'
        for edge in self.edges.values():
            s += str(edge)
        return s
