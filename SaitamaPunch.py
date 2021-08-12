for _ in range(int(input())):
  n, k = map(int, input().split())
  arr = list(map(int, input().split()))
  
  end = arr[0] + k - 1
  t = k
  
  for i in range(1, n):
    temp = arr[i] + k - 1
    if end >= arr[i]:
      t += temp - end
    else:
      t += k
    end = temp
  print(t)  
  
  