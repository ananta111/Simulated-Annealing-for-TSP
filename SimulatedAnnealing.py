import numpy as np


# implementation of simulated annealing
# takes the initial configuration, the graph object, starting temperature T, an temperature change as input
# simulate method of this class takes the number of epochs, runs the algorithm
# and returns a list of path weights seen during the simulation,
# the actual paths associated with those weights, and the final path
class SimulatedAnnealing:
    def __init__(self, initialPath, graph, tempChange, T=5):
        self.graph = graph
        self.path = initialPath
        self.tempChange = tempChange
        self.T = T

    def switchCities(self, path):
        newPath = path[:]
        i, j = np.random.randint(1, len(path) - 1), np.random.randint(1, len(path) - 1)
        newPath[i], newPath[j] = newPath[j], newPath[i]

        return newPath

    def shouldAccept(self, L0, L1, T):
        if L1 < L0:
            return True

        dE = L0 - L1
        prob = np.exp(dE / (T + 0.00))
        randProb = np.random.rand()

        if prob > randProb:
            return True

        return False

    def simulate(self, epochs):
        T = self.T
        path = self.path
        graph = self.graph
        dT = self.tempChange

        weights = [graph.getPathWeight(path)]
        paths = [path]

        for i in range(epochs):
            print("Epoch {} ====================================".format(i))

            L0 = graph.getPathWeight(path)
            newPath = self.switchCities(path)
            L1 = graph.getPathWeight(newPath)

            if self.shouldAccept(L0, L1, T):
                path = newPath
                weights.append(L1)
            else:
                weights.append(L0)

            paths.append(path)

            T = T - dT
            print("Current Weight {}   Current Temp {:.2f}\n".format(graph.getPathWeight(path), T))
        return weights, path, paths

