# All about lists!

listOne = [1, 2, 3, 'hello']
print(listOne)

# Indexing into a List
#print(listOne[2])
#print(listOne[-1])

# Determine the length of a list
#print(len(listOne))

# Printing all items in a list w/o brackets
#for item in listOne:
#    print(item, end=' ')

# Some functions for lists
listOne.reverse()
print(listOne)

listOne.append(100)
print(listOne)

listOne.insert(1, 'Jake')
print(listOne)

# Replace a value using indices
listOne[0] = 1337
print(listOne)
