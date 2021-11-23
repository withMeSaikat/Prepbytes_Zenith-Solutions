class Graph:
  def __init__(self, r, c):
    self.grid = None
    self.row = r
    self.col = c
  def getInput(self):
    self.grid = [None] * self.row
    inp = list(map(int, input().split()))
    for i in range(self.row):
      self.grid[i] = inp[i * self.col:(i + 1) * self.col] 
    # print(self.grid)
    # self.printGrid()
  def noOfComp(self):
    visited = [None] * self.row
    for i in range(self.row):
      visited[i] = [False] * self.col
    
    count = 0
    offsets_r = [0, -1, 0, 1]
    offsets_c = [-1, 0, 1, 0]
    queue = []
    for i in range(self.row):
      for j in range(self.col):
        if visited[i][j] or self.grid[i][j] == 0:
          continue
        count += 1
        queue.append([i, j])
        visited[i][j] = True
        while len(queue) > 0:
          curr_r, curr_c = queue.pop(0)
          for k in range(4):
            nxt_r = curr_r + offsets_r[k]
            if nxt_r >= self.row or nxt_r < 0:
              continue
            
            nxt_c = curr_c + offsets_c[k]
            if nxt_c >= self.col or nxt_c < 0:
              continue
            
            if visited[nxt_r][nxt_c] or self.grid[nxt_r][nxt_c] == 0:
              continue
            visited[nxt_r][nxt_c] = True
            queue.append([nxt_r, nxt_c])
    return count
    
  def printGrid(self, grid = None):
      if grid is None:
          grid = self.grid
      for i in range(self.row):
          for j in range(self.col):
              print(grid[i][j], end = " ")
          print()
            
  def getNearCellUtil(self, x, y):
    visited = [None] * self.row
    for i in range(self.row):
      visited[i] = [False] * self.col
    queue = []
    queue.append([x, y])
    visited[x][y] = True
    while len(queue) > 0:
      curr_r, curr_c = queue.pop(0)
      offset = [(0, -1), (-1, 0), (0, 1), (1, 0)]
      for k in offset:
        nxt_r = curr_r + k[0]
        nxt_c = curr_c + k[1]
        if nxt_r < 0 or nxt_r >= self.row:
          continue
        if nxt_c < 0 or nxt_c >= self.col:
          continue
        if visited[nxt_r][nxt_c]:
          continue
        if self.grid[nxt_r][nxt_c] == 1:
          return abs(x - nxt_r) + abs(y - nxt_c)
        queue.append([nxt_r, nxt_c])
        visited[nxt_r][nxt_c] = True
    return -1
  
  def getNearCell(self):
    res = [None] * self.row
    for i in range(self.row):
      res[i] = [0] * self.col
    
    for i in range(self.row):
      for j in range(self.col):
        if self.grid[i][j] == 1:
          print(res[i][j], end = " ")
        #res[i][j] = self.getNearCellUtil(i, j)
        else:
            print(self.getNearCellUtil(i, j), end=" ")
    print()
  
def main():
  for _ in range(int(input())):
    n, m = map(int, input().split())
    graph = Graph(n, m)
    graph.getInput()
    graph.getNearCell()

# SOLVED
if __name__ == "__main__":
  main()