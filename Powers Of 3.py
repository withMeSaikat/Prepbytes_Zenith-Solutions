from math import log, floor

def log3(n):
    return floor(log(n, 3))
        
def helper(n):
  if n == 0:
    return 1
    
  maxPow = floor(log3(n))
  k = maxPow
  res = 0
  while n > 0 and maxPow >= 0:
    res += 3 ** maxPow
    n -= 3 ** maxPow
    maxPow -= 1
  if n > 0:
      return 3 ** (k + 1)
      
  return res

def helper2(n):
  base = floor(log3(n)) + 1
  res = [None]
  helper3(n, n, 0, base, res)
  return res[0]
  
def helper3(n, curr, ind, mx, res):
  if curr >= n:
    if res[0] is None:
      res[0] = curr
    else:
      res[0] = min(res[0], curr)
  
  if ind > mx:
    return
  
  for i in range(ind, base):
    helper3(n, curr - 3 ** i, i, mx, res)
    helper3(n, curr, i, mx, res)

def createArrays():
  '''
  This function creates two arrays
    1. leftSum = Cumulative sum of sums of powers of 3
    N.B. We have precalculated the maximum sum of 3 (upper value)
    of max range of n
    2. powers = values of powers of 3
  '''
  N = 10 ** 18
  maxPow = floor(log3(N)) + 1
  
  leftSum = [1] * (maxPow + 1)
  powers = [1] * (maxPow + 1)
  for i in range(1, maxPow + 1):
    curr = 3 ** i
    powers[i] = curr
    leftSum[i] = leftSum[i-1] + curr
  return (leftSum, powers)
  
def powerOf3(n, leftSum, powers):
  ind = None
  for i in range(len(leftSum)):
    if leftSum[i] >= n:
      ind = i
      break
  
  res = leftSum[ind]
  
  while ind >= 0:
    if res - powers[ind] >= n:
      res -= powers[ind]
    
    ind -= 1
  return res
  
if __name__ == "__main__":
  leftSum, powers = createArrays()
  
  for _ in range(int(input())):
    n = int(input())
    print(powerOf3(n, leftSum, powers))

  