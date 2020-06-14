class Graph():
    def __init__(self):
        self.numberofnodes = 0
        self.adjacentlist = {}
    
    def __str__(self):
        return str(self.__dict__)

    def addVertex(self,node):
        self.numberofnodes += 1
        self.adjacentlist[node] =[]
    
    def addEdge(self,node1,node2):
        self.adjacentlist[node1].append(node2)
        self.adjacentlist[node2].append(node1)

    def showConnections(self):
        for i in self.adjacentlist:
            print(i,end="-->")
            for j in self.adjacentlist[i]:
                print(j,end=" ")
            print()
m = Graph()
m.addVertex('0')
m.addVertex('1')
m.addVertex('2')
m.addVertex('3')
m.addVertex('4')
m.addVertex('5')
m.addVertex('6')
m.addEdge('3', '1')
m.addEdge('3', '4') 
m.addEdge('4', '2') 
m.addEdge('4', '5') 
m.addEdge('1', '2') 
m.addEdge('1', '0') 
m.addEdge('0', '2') 
m.addEdge('6', '5')
print(m)
print(m.showConnections())
