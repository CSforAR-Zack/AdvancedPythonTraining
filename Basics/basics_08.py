# Slicing and dicing a list

myList = [1,3,3,7,9,22]
newList = myList
print(myList)
print(newList)
newList.append('Cool Beans')
print('------------')
print(myList)
print(newList)
print('------------')
# Behold! List Slicing!
thirdList = myList[:]
thirdList.pop()
print(myList)
print(thirdList)
print(myList)

print(myList[0:6:2])
print(myList[::-1])