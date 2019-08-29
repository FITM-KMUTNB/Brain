import glob
import os
import datetime
import networkx as nx
import matplotlib.pyplot as plt

MainGraph = nx.Graph()


def main():
    starttime = datetime.datetime.now()
    print('Start Read File GML')
    MainGraph = read_graphfile('Gplay.gml')
    readtime = datetime.datetime.now()
    print('Start plot Graph')
    PGraph = MainGraph.subgraph(['dog', 'baby', 'women'])
    plot_graph(MainGraph)

    print(nx.info(MainGraph))
    print("="*20, 'Timer', "="*20)
    # print time start - finish to calculate time use
    finishtime = datetime.datetime.now()
    print("Start time : ")
    print(starttime.strftime("%Y-%m-%d %H:%M:%S"))
    print("Read time : ")
    print(readtime.strftime("%Y-%m-%d %H:%M:%S"))
    print("Finish time : ")
    print(finishtime.strftime("%Y-%m-%d %H:%M:%S"))
    print("="*20, 'End', "="*20)


# Read Graph from file .gml
def read_graphfile(fname):
    G = nx.read_gml(fname)
    return G


# Plot Graph
def plot_graph(G):

    nx.draw_networkx(G, with_labels=True)
    plt.show()


main()
