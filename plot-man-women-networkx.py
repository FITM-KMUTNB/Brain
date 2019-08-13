import networkx as nx
import matplotlib.pyplot as plt
import datetime

MyBrain = {'man': 3, 'woman': 4, 'year': 1, 'baby': 2}
BrainLink = {'man-woman': 3, 'man-baby': 1, 'man-year': 1, }


# Main function process file in directoty
def main():
    starttime = datetime.datetime.now()

    for wordpair in BrainLink:
        BrainLink[wordpair][1] = caldice(wordpair, BrainLink[wordpair][0])
    print("="*20, 'Summaries', "="*20)
   # print(MyBrain)
   # print(BrainLink)
    print("="*20, 'Summaries', "="*20)
    print("The size of is", MyBrain.__sizeof__(),
          'with :', len(MyBrain), 'words')
    print("The size of is", BrainLink.__sizeof__(),
          'with :', len(BrainLink), 'links')
    print('Top keyword is ', max(MyBrain, key=MyBrain.get),
          'with the value ', max(MyBrain.values()))
    print('Top keyword is ', max(BrainLink, key=BrainLink.get),
          'with the value ', max(BrainLink.values()))
    print('disease value: ', MyBrain['disease'])
    print('people value: ', MyBrain['people'])
    print(xcount)
    print(ycount)

    creategraph()

    # print(BrainGraph.degree())
    # print(BrainGraph.edges())

    print('Create Graph:', BrainGraph.number_of_nodes(),
          'nodes and ', BrainGraph.number_of_edges(), ' links')

    # print(nx.dijkstra_path(BrainGraph, 'disease', 'people'), ' with the lenght of :',
    #      nx.dijkstra_path_length(BrainGraph, 'people', 'fetal', weight='weight'))

    #print(nx.shortest_path(BrainGraph, source='jump', target='child'))
    for C in nx.connected_component_subgraphs(BrainGraph):
        print(nx.average_shortest_path_length(C, weight='weight'))
    print(BrainGraph.edges['disease', 'people']['weight'])

    # Dump edge list to file with '|' delimiter
    fh = open("test.edgelist", 'wb')
    nx.write_edgelist(BrainGraph, fh, delimiter='|')
    nx.write_gml(BrainGraph, "test.gml", stringizer=None)

    finishtime = datetime.datetime.now()
    print("Start time : ")
    print(starttime.strftime("%Y-%m-%d %H:%M:%S"))
    print("Finish time : ")
    print(finishtime.strftime("%Y-%m-%d %H:%M:%S"))

# List all the text file in the directory


nx.draw_networkx(BrainGraph, with_labels=True)
plt.show()
