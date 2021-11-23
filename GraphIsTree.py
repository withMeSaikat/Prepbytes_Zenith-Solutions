class Graph:
  def __init__(self, size):
    self.size = size
    self.vertices = [None] * (self.size)
    for i in range(self.size):
        self.vertices[i] = []
        
  def addEdge(self, u, v):
    if self.vertices[u] is None:
      self.vertices[u] = []
    
    self.vertices[u].append(v)
    
    if self.vertices[v] is None:
      self.vertices[v] = []
    
    self.vertices[v].append(u)

  def findComponents(self):
    visited = [False] * (self.size)
    count = 0
    queue = []
    for i in range(self.size):
      if visited[i]:
        continue
      count += 1
      queue.append(i)
      visited[i] = True
      while len(queue) > 0:
        curr = queue.pop(0)
        neighbors = self.vertices[curr]
        
        for nxt in neighbors:
          if visited[nxt]:
            continue
          queue.append(nxt)
          visited[nxt] = True
          
    return count
  
  def hasCycleBFS(self):
    visited = [False] * self.size
    queue = []
    parent = [-1] * self.size
    for i in range(self.size):
      if visited[i]:
        continue
      queue.append(i)
      visited[i] = True
      while len(queue) > 0:
        curr = queue.pop(0)
        neighbors = self.vertices[curr]
        for nxt in neighbors:
          if parent[curr] == nxt:
              continue
          if visited[nxt]:
            #print("HAS CYCLE")
            return True
            
          parent[nxt] = curr
          queue.append(nxt)
          visited[nxt] = True
    #print("NO CYCLE")
    return False
    
def main():
  for _ in range(int(input())):
    n, e = map(int, input().split())
    graph = Graph(n)
    for i in range(e):
      u, v = map(int, input().split())
      graph.addEdge(u, v)
      
    cnt = graph.findComponents()
    #print(cnt)
    if graph.hasCycleBFS() or cnt > 1:
      print("NO")
    else:
      print("YES")
      
if __name__ == "__main__":
  try:
    main()
  except E as Exception:
    print(E)