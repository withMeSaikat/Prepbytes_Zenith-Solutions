n = int(input())

arr = list(map(int, input().split()))

arr = [(arr[i], i) for i in range(n)]

arr.sort(key = lambda element: element[0])

arr.append((-1, n))

count = 0
d = 0
flag = False

res = []

for i in range(1, n+1):
  if arr[i][0] != arr[i-1][0]:
   
    if not flag:
        res.append((arr[i-1][0], d))
        count += 1
    else:
        flag = False
    d = 0
  else:
    if d == 0:
      d = arr[i][1] - arr[i-1][1]
    elif d != arr[i][1] - arr[i-1][1]:
        flag = True
    
print(count)
for elem in res:
  print(elem[0], elem[1])