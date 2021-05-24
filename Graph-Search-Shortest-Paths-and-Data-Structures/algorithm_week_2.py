import time
import sys
import collections as cl

class graph():

    def __init__(self, size = 0):
        self.vertices = cl.defaultdict(dict)
        self.pathToVertex = cl.defaultdict(int)
        self.pathToVertex[1] = 0
        self.size = 0

    def addVertex(self, vertex, edge, weight=0):
        self.vertices[vertex][edge]=int(weight)
        if vertex != 1:
            self.pathToVertex[vertex] = sys.maxsize

        if self.size < vertex:
            self.size = vertex
        elif self.size < edge:
            self.size = edge

    def calc_dijkstra(self):
        self.weightToVertex= [sys.maxsize-10] * (self.size + 1)
        self.weightToVertex[1] =  0
        all_verteces = [x for x in self.vertices]
        visited_verteces = dict()

        while set(all_verteces) != set(visited_verteces.keys()):
            v = self.weightToVertex.index(min(self.weightToVertex))
            for edge in self.vertices[v]:
                weight = self.vertices[v][edge]
                if self.pathToVertex[edge] >= (self.pathToVertex[v] + weight):
                    self.pathToVertex[edge] = self.pathToVertex[v] + weight
                    self.weightToVertex[edge] = self.pathToVertex[v] + weight
            visited_verteces[v] = True
            self.weightToVertex[v] = sys.maxsize
        for key in [7,37,59,82,99,115,133,165,188,197]:
            print(self.pathToVertex[key], end=', ') 
        print('')

    def __str__(self) -> str:
        return f"Graph (vertices'{self.vertices}' pathToVertex{self.pathToVertex})"

def main():

    gr = graph()

    f = open("dijkstraData.txt", "r")
    for line in f:
        v = line.split()
        for i in v[1:]:
            gr.addVertex(int(v[0]), int(i.split(',')[0]), int(i.split(' ')[1]))
    f.close()

    gr.calc_dijkstra()

if __name__ == '__main__':
    start = time.time()
    main()
    print (time.time() - start)
