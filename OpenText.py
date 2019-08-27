# Centroid
import glob
import os
import datetime
import networkx as nx
import matplotlib.pyplot as plt

MyBrain = dict()
BrainLink = dict()
BrainGraph = nx.Graph()
LargestGraph = nx.Graph()
xcount = 0
ycount = 0


# Main function process file in directoty
def main():
    global LargestGraph
    starttime = datetime.datetime.now()
    print("="*20, 'Begin', "="*20)
    listfile("/Users/anirachmcpro/Desktop/Brain/data222")
    # Put properties dice and cost to BrainLink
    for wordpair in BrainLink:
        BrainLink[wordpair][1] = caldice(wordpair, BrainLink[wordpair][0])
        BrainLink[wordpair][2] = 1/BrainLink[wordpair][1]
    # print(MyBrain)
    # print(BrainLink)

    print("="*20, 'Start create Graph', "="*20)
    # Create graph
    creategraph()

    # Generate connected components and select the largest:
    largest_component = max(nx.connected_components(BrainGraph), key=len)

    # Create a subgraph of G consisting only of this component:
    LargestGraph = BrainGraph.subgraph(largest_component)

    # findcentroid()

    # Dump edge list to file with '|' delimiter
    fh = open("test.edgelist", 'wb')
    nx.write_edgelist(LargestGraph, fh, delimiter='|')
    # Dump Graph to file.gml
    nx.write_gml(LargestGraph, "test.gml", stringizer=None)

    # print Nodes and Links summary
    print("="*20, 'Summaries', "="*20)
    print("The size of Keywords-dict is", MyBrain.__sizeof__(),
          'with :', len(MyBrain), 'words')
    print("The size of Links-dict is", BrainLink.__sizeof__(),
          'with :', len(BrainLink), 'links')
    print('Top Max-keyword is ', max(MyBrain, key=MyBrain.get),
          'with the value ', max(MyBrain.values()))
    print('Top Strongest Link is ', max(BrainLink, key=BrainLink.get),
          'with the value ', max(BrainLink.values()))
    print('The number of nodes in the MainGraph : ',
          LargestGraph.number_of_nodes(), ' nodes')
    print('The number of edges in the MainGraph : ',
          LargestGraph.number_of_edges(), ' edges')

    print("="*20, 'Timer', "="*20)
    # print time start - finish to calculate time use
    finishtime = datetime.datetime.now()
    print("Start time : ")
    print(starttime.strftime("%Y-%m-%d %H:%M:%S"))
    print("Finish time : ")
    print(finishtime.strftime("%Y-%m-%d %H:%M:%S"))
    print("="*20, 'End', "="*20)

   # print(list(LargestGraph.nodes))

    # plot graph
    #nx.draw_networkx(LargestGraph, with_labels=True)
    # plt.show()


# List all the text file in the directory
def listfile(fstr):
    os.chdir(fstr)
    numfile = 0
    for file in glob.glob("*.txt"):
        print("file name: ", file)
        listline(file)
        numfile += 1
        print("-"*20, numfile, "-"*20)


# Read lines from file and clean the line
def listline(fname):
    c_file = open(fname, 'r')

    # Read all the lines from the file.
    for line in c_file:
        # remove |NN and |NP
        nline = line.replace("|NN", "")
        pline = nline.replace("|NP", "")
        # print(pline)
        # process line
        processline(pline)

    c_file.close()


# Processing line
def processline(w_line):
    global MyBrain
    global BrainLink
    global xcount
    global ycount
    wordlists = w_line.split()
    # remove duplicate words
    wordlists = list(dict.fromkeys(wordlists))
    # count specific words
    xcount += wordlists.count('disease')
    ycount += wordlists.count('people')
    # count word frequencies
    for word in wordlists:
        if word in MyBrain.keys():
            MyBrain[word] += 1
        else:
            MyBrain[word] = 1
    # Count word_pairs frequencies
    for i in range(len(wordlists)):
        if i+1 == len(wordlists):
            break
        for j in range(i, len(wordlists)):
            if j+1 == len(wordlists):
                break
            if wordlists[i] == wordlists[j+1]:
                continue
            # create link pair with the less value word first
            if wordlists[i] < wordlists[j+1]:
                word_pair = wordlists[i]+'|' + wordlists[j+1]
            else:
                word_pair = wordlists[j+1]+'|' + wordlists[i]

            if word_pair in BrainLink:
                BrainLink[word_pair][0] += 1
            else:
                BrainLink[word_pair] = [1, 0.0, 0.0]


# calculate Dice-coefficien using formular
# 2*co-occurences count / count of word a + count of word b
def caldice(wordlink, coocvalue):
    global MyBrain
    global BrainLink

    wordlist = wordlink.split('|')
    dicevalue = 2*coocvalue / (MyBrain[wordlist[0]] + MyBrain[wordlist[1]])
    if dicevalue > 1:
        return 1
    else:
        return dicevalue


# Next_Step Try to considering Teta = values to create only important nodes and links
def creategraph():
    global MyBrain
    global BrainLink
    global BrainGraph

    for wnode in MyBrain:
        BrainGraph.add_node(wnode, feq=MyBrain[wnode])

    for wordlink in BrainLink:
        wordlist = wordlink.split('|')
        BrainGraph.add_edge(wordlist[0], wordlist[1],
                            weight=BrainLink[wordlink][0], dice=BrainLink[wordlink][1], cost=BrainLink[wordlink][2])


# for each group
    # for each member of the group
        # get the distance of shortest paths to all the other members of the group
        # sum this distances
    # find the node with the minimal summed distance > this is the new centroid of the group

def findcentroid():

    global LargestGraph

    final_avg = 999999999.99
    final_key = ''
    # find node shortest path to all nodes
    word_allSP = dict(nx.shortest_path_length(LargestGraph, weight='cost'))

    for key in word_allSP:
        avg_nodeSP = sum(word_allSP[key].values())/(len(word_allSP[key]))
        if final_avg > avg_nodeSP:
            final_avg = avg_nodeSP
            final_key = key

    print('The centroid is : ', final_key, final_avg)


# Process raw text file to the noun only (may be nltk needed)
def processtxtfile():
    pass


# To find each document centroid for referencing
def document_centroid():
    pass


# Call main function.
main()
