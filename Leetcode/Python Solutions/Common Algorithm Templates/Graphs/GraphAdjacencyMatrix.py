class Graph(object):
    def __init__(self, size):
        self.adjmatrix = []
        for i in range(size):
            self.adjmatrix.append([0 for i in range(size)])
        self.size = size

    def addEdge(self, v1, v2):
        self.adjmatrix[v1][v2] = 1
        self.adjmatrix[v2][v1] = 1
    
    def removeEdge(self, v1, v2):
        if self.adjmatrix[v1][v2] == 0:
            return
        self.adjmatrix[v1][v2] = 0
        self.adjmatrix[v2][v1] = 0
    
    def len(self):
        return self.size

    def hasEdge(self, v1, v2):
        return True if self.adjmatrix[v1][v2] == 1 else False
    
    def toString(self):
        for row in self.adjmatrix:
            for val in row:
                print('{:4}'.format(val)),
            print()
    
def main():
        g = Graph(5)
        g.addEdge(0, 1);
        g.addEdge(0, 2);
        g.addEdge(1, 2);
        g.addEdge(2, 0);
        g.addEdge(2, 3);

        print(g.hasEdge(2,0))
    
        g.toString()
            
if __name__ == '__main__':
   main()
