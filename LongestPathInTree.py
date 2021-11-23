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
  
  def findLongestPath(self):
    dp = [0] * self.size
    visited = [False] * self.size
    parent = [-1] * self.size
    for i in range(self.size):
      if visited[i]:
        continue
      res = self.findLongestPathUtil(i, dp, visited, parent)
    return max(dp)

  def findLongestPathUtil(self, u, dp, visited, parent):
    if visited[u]:
      return dp[u]
    
    neighbors = self.vertices[u]
    max_dist = 0
    for nxt in neighbors:
      if parent[u] == nxt:
        continue
      parent[nxt] = u
      temp = 1 + self.findLongestPathUtil(nxt, dp, visited, parent)
      max_dist = max(temp, max_dist)
    dp[u] = max_dist
    visited[u] = True
    return dp[u]
  def findLongestPathBFS(self):
    mx = 0
    for i in range(self.size):
      p = self.findLongestPathBFSUtil(i)
      mx = max(mx, p)
    return mx
    
  def findLongestPathBFSUtil(self, u):
    visited = [False] * self.size
    level = [-1] * self.size
    queue = []
    parent = [-1] * self.size
    
    queue.append(u)
    visited[u] = True
    level[u] = 0
    while len(queue) > 0:
      curr = queue.pop(0)
      neighbors = self.vertices[curr]
      for nxt in neighbors:
        if visited[nxt]:
          continue
        parent[nxt] = curr
        level[nxt] = level[parent[nxt]] + 1
        visited[nxt] = True
        queue.append(nxt)
      
    return max(level)
          
# SOLVED
def main():
  for _ in range(int(input())):
    n, e = map(int, input().split())
    graph = Graph(n)
    for i in range(e):
      u, v = map(int, input().split())
      graph.addEdge(u, v)
    mx = graph.findLongestPathBFS()
    print(mx)
      
      
if __name__ == "__main__":
  try:
    main()
  except E as Exception:
    print(E)
        