# This program uses the for loop to read
# all of the .txt file.
# MyBrain = {'man': 3, 'woman': 4, 'year': 1, 'baby': 2}
# BrainLink = {'man-woman': 3, 'man-baby': 1, 'man-year': 1}
import glob
import os

MyBrain = dict()
BrianLink = dict()

# Main function process file in directoty


def main():
    listfile("/Users/anirachmcpro/Desktop/Brain")
    print("="*20, 'Summaries', "="*20)
    print(MyBrain)
    print(BrianLink)


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
        print(line)
        processline(line)
        print(MyBrain)
    # Close the file.
    c_file.close()

# Processing line


def processline(w_line):
    global MyBrain
    global BrianLink
    wordlists = w_line.split()
    print(wordlists)
    for word in wordlists:
        count = wordlists.count(word)

        # Count Word frequencies
        if word in MyBrain.keys():
            MyBrain[word] += count
        else:
            MyBrain[word] = count
        # Count word_pairs frequencies
        # here have to be functuion swap compare
        # and pair_word order by less-more
        if link_exist(word_pair):
            BrainLink[word_pair] += count
        else:
            Brain_Link[word_pair] = count


def link_exist(wordlink):
    global BrianLink
    wlist = wordlink.split('-')
    wlrev = wlist[1]+wlist[0]
    if wordlink in BrianLink.keys():
        return True
    elif wlrev in BrainLink.keys():
        return True
    else:
        return False


# Call the main function.
main()
