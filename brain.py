MyBrain = {'man': 3, 'woman': 4, 'year': 1, 'baby': 2}
BrainLink = {'man-woman': 3, 'man-baby': 1, 'man-year': 1}
print(MyBrain.items())
print(MyBrain.values())
print(MyBrain.keys())
if 'man-baby' in BrainLink:
    print(MyBrain.__sizeof__())
print(max(MyBrain.values()))


inputStr = "pynativepynvepynative"
countDict = dict()
for char in inputStr:
    count = inputStr.count(char)
    countDict[char] = count
print(countDict)
