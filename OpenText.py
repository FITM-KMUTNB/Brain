# This program uses the for loop to read
# all of the .txt file.
import glob
import os


# Main function process file in directoty
def main():
    listfile("/Users/anirachmcpro/Desktop/Brain")


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
    # Close the file.
    c_file.close()


# Call the main function.
main()
