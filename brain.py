MyBrain = {'man': 3, 'woman': 4, 'year': 1, 'baby': 2}
BrainLink = {'man-woman': 3, 'man-baby': 1, 'man-year': 1}
print(MyBrain.items())
print(MyBrain.values())
print(MyBrain.keys())
if 'man-baby' in BrainLink:
    print("The size of is", MyBrain.__sizeof__(),
          'with :', len(MyBrain), 'words')
print('Top keyword is ', max(MyBrain, key=MyBrain.get),
      'with the value ', max(MyBrain.values()))
