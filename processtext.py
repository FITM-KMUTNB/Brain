# This program uses the for loop to read
# all of the .txt file.
# MyBrain = {'man': 3, 'woman': 4, 'year': 1, 'baby': 2}
# BrainLink = {'man-woman': 3, 'man-baby': 1, 'man-year': 1}
import glob
import os

MyBrain = dict()
BrainLink = dict()

# Main function process file in directoty


def main():
    listfile("/Users/anirachmcpro/Desktop/Brain/Corpus")
    print("="*20, 'Summaries', "="*20)
    print(MyBrain)
    print(BrainLink)
    print("="*20, 'Summaries', "="*20)
    print("The size of is", MyBrain.__sizeof__(),
          'with :', len(MyBrain), 'words')
    print("The size of is", BrainLink.__sizeof__(),
          'with :', len(BrainLink), 'links')


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


# Neo4j - Create graph database
def create_node():
    global MyBrain
    pass


def create_link():
    global BrainLink
    pass


# Call the main function.
main()
