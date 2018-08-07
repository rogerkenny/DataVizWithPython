class Graph:
    def __init__(self, size):
        self.nodes = [None] * size 
        
    def connect(self, x, y):
        if self.nodes[x] == None:
            self.nodes[x] = [y]
        else:
            self.nodes[x].append(y)
        
        if self.nodes[y] == None:
            self.nodes[y] = [x]
        else:
            self.nodes[y].append(x)
        
    
    def find_all_distances(self, start):
        distances = [-1] * len(self.nodes)
        distances[start] = 0
        edgeVal = 6
        visited = {start}
        queue = [start]
        while len(queue) > 0:
            current = queue.pop(0)
            if self.nodes[current] == None:
                continue
            for e in self.nodes[current]:
                if not e in visited:
                    queue.append(e)
                    distances[e] = distances[current] + edgeVal
                    visited.add(e)
        o = ''
        for i, d in enumerate(distances):
            if i != start:
                o += "{} ".format(d)
        print (o)
        return distances


fi = open('bfs_in_001.txt', 'r')


t = int(fi.readline().rstrip())
for i in range(t):
    n,m = [int(value) for value in fi.readline().split()]
    graph = Graph(n)
    for i in range(m):
        x,y = [int(x) for x in fi.readline().split()]
        graph.connect(x-1,y-1) 
    s = int(fi.readline())
    graph.find_all_distances(s-1)