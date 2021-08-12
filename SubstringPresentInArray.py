def solution(a, b, n, m):
  if m > n:
    return False
  
  i = 0
  lastI = -1
  j = 0
  
  while(j < m):
    i = lastI + 1
    found = False
    
    while(i < n):
      if a[i] == b[j]:
        lastI = i
        found = True
        break
        if n - i - 1 < m - j - 1:
          return False
      i += 1
    
    if not found:
      return False
    j += 1
  
  return True

# Solved
def main():
  for _ in range(int(input())):
    n = int(input())
    a = list(map(int, input().strip().split()))
    m = int(input())
    b = list(map(int, input().strip().split()))
    
    if(solution(a, b, n, m)):
      print('YES')
    else:
      print('NO')

if __name__ == '__main__':
  main()
  
# 2
# 6
# 4 8 2 9 1 6
# 3
# 8 1 6
# 4
# 1 2 3 4
# 4
# 5 6 7 8
  
  
  
  
  
  
  
  
          