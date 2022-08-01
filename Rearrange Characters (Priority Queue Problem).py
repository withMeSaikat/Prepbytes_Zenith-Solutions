from heapq import heapify, heappop, heappush
class MyList(list):
    def __lt__(self, other):
        return self[1] < other[1]
        
for _ in range(int(input())):
  s = input().strip()
  count = [0] * 26
  for ch in s:
    count[ord(ch) - 97] += 1
  
  heap = []
  heapify(heap)
  for i in range(26):
    if count[i] == 0:
      continue
    heappush(heap, MyList([chr(i+97), i]))
  
  res = ""
  while len(heap) > 0:
    curr = heappop(heap)
    curr_char, priority = curr
    
    res = res + curr_char
    count[ord(curr_char) - 97] -= 1
    if count[ord(curr_char) - 97] > 0: 
      if len(heap) == 0:
        res = "-1"
        break
      
      nxt = heappop(heap)
      heappush(heap, nxt)
      curr[1] = nxt[1]
      heappush(heap, curr)
  print(res)
    