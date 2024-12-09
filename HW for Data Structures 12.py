class Graph:
    __n = 0
    __g = [[0 for x in range(10)] for y in range(10)]
    def __init__(self,x):
        self.__n = x
        for i in range(0,self.__n):
            for j in range(0,self.__n):
                self.__g[i][j] = 0


    def add_edge(self,x,y):
        if (x>=self.__n) or (y>=self.__n):
            print("vertex does not exist")
        if (x==y):
            print("Same vertexs!")
        else:
            self.__g[y][x] = 1
            self.__g[x][y] = 1

    def display_matrix(self):
        for i in range(0,self.__n):
            print()
            for j in range(0,self.__n):
                print("", self.__g[i][j], end="")

    def userInput(self):
        #self.__g = [[0] * x for _ in range(x)]
        while True:
            userInt = input("Enter the edges (For example, '3 4' or 0 if you're done")
            if userInt == "0":
                break
            else:
                x,y = map(int, userInt.split())
                self.add_edge(x,y)

    def removeVertex(self,x):
        if (x > self.__n):
            print("Vertex not present!")
        else:
            while (x<self.__n):
                for i in range(0,self.__n):
                    self.__g[i][x] = self.__g[i][x+1]
                for i in range(0,self.__n):
                    self.__g[x][i] = self.__g[x+1][i]
                x = x + 1
            self.__n = self.__n - 1
obj = Graph(6)
obj.userInput()
print("Before removal")
obj.display_matrix()
obj.removeVertex(4)
print("\nAfter removal")
obj.display_matrix()

