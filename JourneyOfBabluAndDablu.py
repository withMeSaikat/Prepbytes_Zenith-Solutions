import math

def search(arr, key):
    for i in range(len(arr)):
        if arr[i][0] == key:
            return i 

left = [(7, 'SL'), (3, 'UB'), (2, 'MB'), (1, 'LB')]
right = [(8, 'SU'), (6, 'UB'), (5, 'MB'), (4, 'LB')]
  
def Solution(n):
  n_compartment = math.ceil(n / 8)
  n -= 8 * (n_compartment - 1)
  # print("n: ", n)
  
  if n in [7, 3, 2, 1]:
    ind = search(left, n)
    return (str(right[ind][0] + 8 * (n_compartment - 1)) + right[ind][1])
  else:
    ind = search(right, n)
    return (str(left[ind][0] + 8 * (n_compartment - 1)) + left[ind][1])

for _ in range(int(input())):
  n = int(input())
  print(Solution(n))
  

def demoSol(n):
  while n > 8:
    n -= 8
  if n in [7, 3, 2, 1]:
    ind = search(left, n)
    return (str(right[ind][0]) + right[ind][1])
  else:
    ind = search(right, n)
    return (str(left[ind][0]) + left[ind][1])

  

import random

def Test():
  T = random.randint(1, 30)
  while T > 0:
    n = random.randint(10000, 1000000)
    demSol = demoSol(n)
    sol = Solution(n)
    if demSol != sol:
      print("Demosol:", demSol)
      print("Solution:", sol)
      print("n:", n)
    else:
      print("PASSED!")

# Test()

