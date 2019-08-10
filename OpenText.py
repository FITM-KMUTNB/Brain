# This program uses the for loop to read
# all of the .txt file.
# MyBrain = {'man': 3, 'woman': 4, 'year': 1, 'baby': 2}
# BrainLink = {'man-woman': 3, 'man-baby': 1, 'man-year': 1}
import glob
import os
import networkx as nx

MyBrain = dict()
BrainLink = dict()
BrainGraph = nx.Graph()


# Main function process file in directoty


def main():
    listfile("/Users/anirachmcpro/Desktop/Brain")
    print("="*20, 'Summaries', "="*20)
    print(MyBrain)
    print(BrainLink)
    creategraph()
    list(BrainGraph)


# List all the text file in the directory
def listfile(fstr):
    os.chdir(fstr)
    numfile = 0
    for file in glob.glob("*.txt"):
        print("file name: ", file)
        listline(file)
        numfile += 1
        print("-"*20, numfile, "-"*20)


# Open each file and process line by line
def listline(fname):
    c_file = open(fname, 'r')
    # Read all the lines from the file.
    for line in c_file:
        processline(line)
    c_file.close()


# Processing line
def processline(w_line):
    global MyBrain
    global BrainLink
    wordlists = w_line.split()
    # count word frequencies
    for word in wordlists:
        count = wordlists.count(word)
        if word in MyBrain.keys():
            MyBrain[word] += count
        else:
            MyBrain[word] = count
    # Count word_pairs frequencies
    for i in range(len(wordlists)):
        if i+1 == len(wordlists):
            break
        for j in range(i, len(wordlists)):
            if j+1 == len(wordlists):
                break
            word_pair = wordlists[i]+'-' + wordlists[j+1]
            if link_exist(word_pair):
                BrainLink[word_pair] += count
            else:
                BrainLink[word_pair] = count


def link_exist(wordlink):
    global BrainLink
    wlist = wordlink.split('-')
    wlrev = wlist[1]+wlist[0]
    if wordlink in BrainLink.keys():
        return True
    elif wlrev in BrainLink.keys():
        return True
    else:
        return False


def creategraph():
    global MyBrain
    global BrainLink
    global BrainGraph
    edgecount = 0
    nodecount = 0
    for wnode in MyBrain:
        nodecount += 1
        BrainGraph.add_node(wnode, size=MyBrain[wnode])
    print('create :', nodecount, ' nodes')

    for wordlink in BrainLink:
        wordlist = wordlink.split('-')
        print(wordlist)
        print(BrainLink[wordlink])
        edgecount += 1
        BrainGraph.add_edge(wordlist[0], wordlist[1],
                            weight=BrainLink[wordlink])
    print('creaate :', edgecount, ' links')


# Call the main function.
main()
