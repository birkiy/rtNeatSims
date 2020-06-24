class Node:
    def __init__(self, id, type=0):
        self.id = id
        self.bias = 0
        self.type = type

    def __hash__(self):
        return self.id

    def __str__(self):
        return f'''
ID #{self.id}
Bias: {self.bias}
Type: {'input' if self.type == -1 else 'output' if self.type == 1 else 'hidden'}
        '''
