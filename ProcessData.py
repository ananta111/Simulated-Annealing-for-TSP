import re


# Processes the space-separated matrix based representation of a graph
# to produce a list of edges in (source, destination, weight) format
class ProcessData:
    def __init__(self, dim, fileName):
        self.fileName = fileName
        self.tspData = None
        self.edges = None
        self.nodes = [i for i in range(dim)]
        self.matrix = None
        self.edges = self.getEdges()

    def processFile(self):
        with open(self.fileName) as f:
            lines = f.read().splitlines()

        matrix = []

        for line in lines:
            temp = line.strip(" ")
            temp = re.split(r'\s+', temp)
            matrix.append(temp)

        self.matrix = matrix
        return matrix

    def getEdges(self):
        edges = []
        matrix = self.processFile()

        # for row in matrix:
        #    print(row)

        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if i != j:
                    u, v, w = i, j, int(matrix[i][j])
                    edges.append((u, v, w))

        return edges


# returns the Process Data object given a file path of the dataset and the number of nodes
def getSampleData(numNodes, filePath):
    p = ProcessData(numNodes, filePath)
    return p












