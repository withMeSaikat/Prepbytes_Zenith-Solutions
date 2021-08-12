def isUnique(num):
  num = str(num)
  for i in range(0, len(num)):
    for j in range(i+1, len(num)):
      if num[i] == num[j]:
        return False
  return True

n = int(input())

arr = [int(input()) for i in range(n)]

for num in arr:
  flag = True
  while flag:
    num += 1
    if(isUnique(num)):
      print(num)
      flag = False