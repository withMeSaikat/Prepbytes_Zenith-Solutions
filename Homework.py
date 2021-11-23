class Graph:
  def __init__(self, size, edges):
    self.edges = edges
    self.size = size
    self.vertices = [None] * self.size
    for i in range(self.size):
      self.vertices[i] = []
  
  def getInput(self):
    for i in range(self.edges):
      u, v = map(int, input().split())
      self.vertices[u].append(v)
  
  def hasCycleUtil(self, u, visited, stack):
    visited[u] = True
    stack[u] = True
    
    for nxt in self.vertices[u]:
      if not visited[nxt]:
        if self.hasCycleUtil(nxt, visited, stack):
          return True
      elif stack[nxt]:
        return True
    stack[u] = False
    return False
  
  def hasCycle(self):
    visited = [False] * self.size
    stack = [False] * self.size
    for i in range(self.size):
      if visited[i]:
        continue
      if self.hasCycleUtil(i, visited, stack):
        return True
    return False

def main():
  n, e = map(int, input().split())
  