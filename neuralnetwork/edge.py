class Edge:
    def __init__(self, begin, end):
        self.weight = 0
        self.disabled = False
        self.begin = begin
        self.end = end

    def copy(self):
        edge = Edge(self.begin, self.end)
        edge.weight = self.weight
        edge.disabled = self.disabled
        return edge

    def copy_with_begin(self, begin):
        edge = Edge(begin, self.end)
        edge.weight = self.weight
        edge.disabled = self.disabled
        return edge

    def copy_with_end(self, end):
        edge = Edge(self.begin, end)
        edge.weight = self.weight
        edge.disabled = self.disabled
        return edge

    def __eq__(self, other):
        return self.begin == other.begin and self.end == other.end

    def __str__(self):
        return f'''
From: ID #{self.begin}
To: ID #{self.end}
Weight: {self.weight}
Disabled: {self.disabled}
        '''
