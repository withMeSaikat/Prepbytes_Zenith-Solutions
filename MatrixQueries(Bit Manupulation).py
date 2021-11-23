def printMatrix(arr, n, row_l, row_h, col_l, col_h, c):
  for i in range(n):
    for j in range(n):
      if (i >= row_l and i <= row_h) and (j >= col_l and j <= col_h):
        print(arr[i][j] ^ c, end=" ")
      else:
        print(arr[i][j], end=" ")
    print()

def processQueries(queries, n):
  row = [0] * n
  column = [0] * n
  for query in queries:
    f, x, y, c = query
    if f == 1:
      for i in range(x - 1, y):
        row[i] ^= c
    else:
      for i in range(x - 1, y):
        column[i] ^= c
  return (row, column)

# SOLVED
def main():
  n = int(input())
  arr = [0] * n
  for i in range(n):
    arr[i] = list(map(int, input().split()))
  
  q = int(input())
  queries = [0] * q
  for i in range(q):
    queries[i] = map(int, input().split())
  row, column = processQueries(queries, n)
  for i in range(n):
    for j in range(n):
      print(arr[i][j] ^ row[i] ^ column[j], end=" ")
    print()
if __name__ == "__main__":
  try:
    main()
  except Exception as E:
    print(E)