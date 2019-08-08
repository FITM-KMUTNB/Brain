# This program uses the for loop to read
# all of the .txt file.
# MyBrain = {'man': 3, 'woman': 4, 'year': 1, 'baby': 2}
# BrainLink = {'man-woman': 3, 'man-baby': 1, 'man-year': 1}
import glob
import os
import re

MyBrain = dict()
BrainLink = dict()
BrainLinkDice = dict()
xcount = 0
ycount = 0

# Main function process file in directoty


def main():
    listfile("/Users/anirachmcpro/Desktop/Brain/Corpus")
    print("="*20, 'Summaries', "="*20)
   # print(MyBrain)
    print(BrainLink)
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
    print('lyme value: ', MyBrain['lyme'])
    print(xcount)
    print(ycount)

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
        # remove |NN and |NP
        nline = line.replace("|NN", "")
        pline = nline.replace("|NP", "")
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
    ycount += wordlists.count('lyme')
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

            if link_exist(word_pair):
                BrainLink[word_pair] += 1
            else:
                BrainLink[word_pair] = 1


def link_exist(wordlink):
    global BrainLink
    wlist = wordlink.split('|')
    wlrev = wlist[1]+wlist[0]
    if wordlink in BrainLink.keys():
        return True
    elif wlrev in BrainLink.keys():
        return True
    else:
        return False

# calculate Dice-coefficien using formular
# 2*co-occurences count / count of word a + count of word b


def caldice(wordlink, coocvalue):
    global MyBrain
    global BrainLink
    global BrainLinkDice

    pass


# Neo4j - Create graph database
def create_node():
    global MyBrain
    pass


def create_link():
    global BrainLink
    pass


# Call the main function.
main()
