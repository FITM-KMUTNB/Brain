import networkx as nx
import datetime

starttime = datetime.datetime.now()

H = nx.read_gml('/Users/anirachmcpro/Desktop/Brain/Corpus/test.gml')

# print(H.degree())

finishtime = datetime.datetime.now()
print("Start time : ")
print(starttime.strftime("%Y-%m-%d %H:%M:%S"))
print("Finish time : ")
print(finishtime.strftime("%Y-%m-%d %H:%M:%S"))
