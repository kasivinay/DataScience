myUniqueList = []
myLeftovers = []

def addToList(thing):
    if thing in myUniqueList:
        addToLeftovers(thing)
        return False
    else:
        myUniqueList.append(thing)
        return True
def addToLeftovers(thing):
  myLeftovers.append(thing)
print(myUniqueList)
print(myLeftovers)
print(addToList("thing"))
print(addToList("dog"))
print(addToList("thing"))
print(myUniqueList)
print(myLeftovers)

