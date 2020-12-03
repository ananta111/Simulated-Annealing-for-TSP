from collections import defaultdict


# Adjacency list based implementation of a graph
class Graph:
    def __init__(self, nodes, edges):
        self.nodes = nodes
        self.edges = edges
        self.graph = defaultdict(list)
        self.edgeWeights = defaultdict(int)
        self.processEdges(edges)

    def processEdges(self, edges):
        for idx, (u, v, w) in enumerate(edges):
            self.graph[u].append((v, w))
            self.edgeWeights[(u, v)] = w

    def getPathWeight(self, path):
        weight = 0
        for i in range(len(path) - 1):
            weight += self.edgeWeights[(path[i], path[i + 1])]

        return weight

    def getEdgesFromPath(self, path):
        edges = []
        for i in range(len(path) - 1):
            u, v = path[i], path[i + 1]
            w = self.getPathWeight((u, v))
            edges.append((u, v, w))

        return edges

    def printPath(self, path):
        for node in path:
            print(str(node), end=" to ")

        pathWeight = self.getPathWeight(path)
        print(" Total path weight {}\n".format(pathWeight))

