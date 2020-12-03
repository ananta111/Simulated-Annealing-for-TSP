from Graph import Graph
from SimulatedAnnealing import SimulatedAnnealing
import matplotlib.pyplot as plt
from Visualize import Animate
import ProcessData as pd
import random


# Creates a complete graph with random edge  weights given a list of nodes
def assignRandomWeights(nodes):
    edges = []
    visited = set()
    for i in range(len(nodes)):
        for j in range(len(nodes)):
            randomWeight = random.randint(5, 50)
            if i != j and (i, j) not in visited:
                edge = (nodes[i], nodes[j], randomWeight)
                rEdge = (nodes[j], nodes[i], randomWeight)
                edges.append(edge)
                edges.append(rEdge)
                visited.add((i, j))
                visited.add((j, i))

    return edges


def run():
    plt.clf()
    print("======= Simulated Annealing for TS P=========")
    print ("Three datasets are available: 26 cities, 42 cities, and 48 cities")
    print("Enter 26, 42, or 48")
    numNodes = int(input())
    dataPath = "./testData/testdata" + str(numNodes) + ".txt"

    print("Enter starting temperature T")
    T = int(input())

    print ("Enter the number of epochs")
    epochs = int(input())

    print("Enter the change in temperature after every epoch (usually very low like 0.001)")
    tempChange = float(input())

    dataset = pd.getSampleData(numNodes, dataPath)  # 2000

    # Processed data and graph creation
    edges = dataset.edges
    nodes = dataset.nodes
    graph = Graph(nodes, edges)

    # ending the tour with the starting node
    initialPath = nodes[:] + [nodes[0]]

    # simulated annealing
    sa = SimulatedAnnealing(initialPath, graph, tempChange, T=T)

    print ("Starting Simulated Annealing for " + dataPath + "\n")

    # recorded weights, final path, and observed paths
    weights, path, paths = sa.simulate(epochs=epochs)

    print("Optimized Path: ", path)
    # the last weight of the simulation is the final path weight
    print("Optimized Path Weight: ", weights[-1])

    # plotting cost curve and drawing graph
    visualise = Animate(edges, weights)

    print("Do you want to save these figures? Enter Y or N")
    saveFig = input()

    visualise.drawPath(path, graph, saveFig=(saveFig == "Y"))
    visualise.plotCost(saveFig=(saveFig == "Y"))



if __name__ == '__main__':
    run()










