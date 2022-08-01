class Graph:
  def __init__(self, size):
    self.size = size
    self.vertices = [None] * self.size
    for i in range(self.size):
      self.vertices[i] = []
  
  def addEdge(self, u, v):
    self.vertices[u].append(v)
    #self.vertices[v].append(u)
  
  def getLevel(self, u):
    level = [-1] * self.size
    queue = []
    queue.append(u)
    level[u] = 0
    while len(queue) > 0:
      curr = queue.pop(0)
      neighbors = self.vertices[curr]
      for nxt in neighbors:
        if level[nxt] != -1:
          continue
        queue.append(nxt)
        level[nxt] = level[curr] + 1
        if nxt == self.size - 1:
          return level[nxt]
          
    return level[self.size-1]
    
def getCount(arr, n):
  count = {}
  for i in range(n):
    if int(arr[i]) not in count:
      count[int(arr[i])] = []
    count[int(arr[i])].append(i)
  
  return count

def arrToGraph(arr):
  n = len(arr)
  indices = getCount(arr, n)
  graph = Graph(n)
  for i in range(n):
    if i != 0 and arr[i] != arr[i-1]:
      graph.addEdge(i, i - 1)
    if i != n - 1 and arr[i] != arr[i+1]:
      graph.addEdge(i, i + 1)
    for indice in indices[int(arr[i])]:
      if i != indice:
        graph.addEdge(i, indice)
  print(graph.getLevel(0))

def getRes(arr):
  n = len(arr)
  indices = getCount(arr, n)
  
  # BFS
  level = [-1] * n
  queue = []
  queue.append(0)
  level[0] = 0
  while len(queue) > 0:
    currIndex = queue.pop(0)
    # Exploring the left and right 
    if currIndex > 0 and level[currIndex - 1] == -1:
      queue.append(currIndex - 1)
      level[currIndex - 1] = level[currIndex] + 1
    
    if currIndex < n - 1 and level[currIndex + 1] == -1:
      queue.append(currIndex + 1)
      level[currIndex + 1] = level[currIndex] + 1
    
    # Exploring similer digit indexes:
    for index in indices[int(arr[currIndex])]:
      if level[index] != -1 or index == currIndex:
        continue
      queue.append(index)
      level[index] = level[currIndex] + 1
      
  print(level[n-1])

# SOLVED

def main():
  s = input()
  getRes(s)
  
if __name__ == "__main__":
  main()