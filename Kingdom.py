class Graph:
  def __init__(self, r, c):
    self.grid = None
    self.row = r
    self.col = c
  def getInput(self):
    self.grid = [None] * self.row
    for i in range(self.row):
      self.grid[i] = list(map(int, input().split()))
    
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

# SOLVED
def main():
  # for _ in range(int(input())):
  n, m = map(int, input().split())
  graph = Graph(n, m)
  graph.getInput()
  print(graph.noOfComp())

if __name__ == "__main__":
  main()