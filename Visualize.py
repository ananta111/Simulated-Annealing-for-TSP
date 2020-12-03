import networkx as nx
import matplotlib.pyplot as plt


# Utilities to plot cost (path weights) and to draw the given graph
# Takes the edges of the original graph and the weights seen during the simulation as inputs
class Animate:
    def __init__(self, edges, weights):
        self.edges = edges
        self.weights = weights
        self.G = nx.Graph()
        # self.G.add_weighted_edges_from(edges)


    # TODO: Future Work: use networkx library to generate a video of how different hamiltonian tours were explored
    # during the simulation

    # def animate(self, i):
    #     edges = self.graph.getEdgesFromPath(self.paths[i])
    #     self.G.add_weighted_edges_from(edges)
    #     fig = pylab.figure()
    #     nx.draw_random(self.G, with_labels=True, node_color="yellow")
    #     labels = nx.get_edge_attributes(self.G, 'weight')
    #     nx.draw_networkx_edge_labels(self.G, pos=nx.spring_layout(self.G), edge_labels=labels)
    #     return fig
    #
    # def start(self):
    #     for i in range(len(self.paths)):
    #         fig = self.animate(i)
    #         fig.canvas.draw()
    #         pylab.pause(0.3)
    #         self.G.clear()
    #         pylab.close(fig)


    def drawGraph(self):
        nx.draw_spring(self.G, with_labels=True, node_color="yellow")
        plt.show()

    def drawPath(self, path, graph, saveFig=False):
        pathEdges = graph.getEdgesFromPath(path)
        for idx, (u, v, w) in enumerate(self.edges):
            if (u, v, w) in pathEdges or (v, u, w) in pathEdges:
                if pathEdges[-1] == (u, v, w) or pathEdges[-1] == (v, u, w):
                    self.G.add_edge(u, v, color="black", weight=2)
                elif pathEdges[0] == (u, v, w) or pathEdges[0] == (v, u, w):
                    self.G.add_edge(u, v, color="r", weight=2)
                else:
                    self.G.add_edge(u, v, color="r", weight=1)
            else:
                self.G.add_edge(u, v, color="b", weight=0.1)

        colors = nx.get_edge_attributes(self.G, 'color').values()
        weights = nx.get_edge_attributes(self.G, 'weight').values()

        pos = nx.spring_layout(self.G)
        nx.draw(self.G, pos,
                edge_color=colors,
                width=list(weights),
                with_labels=True,
                node_color='lightgreen')
        if saveFig:
            figName = "graphdraw" + str(len(path)) + ".png"
            plt.savefig(figName)
        plt.show()





    def plotCost(self, saveFig=False):
        plt.xlabel("Epoch")
        plt.ylabel("Path Weight")
        plt.plot(self.weights)
        if saveFig:
            figName = "costcurve" + str(len(self.edges)) + ".png"
            plt.savefig(figName)
        plt.show()



