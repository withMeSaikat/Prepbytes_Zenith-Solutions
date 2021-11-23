def main():
  for _ in range(int(input())):
    n = int(input())
    arr = list(map(int, input().split()))
    start = 0
    end = n - 1
    res = -1
    while end >= start:
      mid = start + ((end - start) // 2)
      if arr[mid] == 1:
        if (mid - 1 >= 0 and arr[mid - 1] == 0) or mid == 0:
          res = mid
          break
        else:
          end = mid - 1
          continue
      if arr[mid] == 0:
        if mid + 1 < n  and arr[mid + 1] == 1:
          res = mid + 1
          break
        else:
          start = mid + 1
          continue
    
    print(res)

if __name__ == '__main__':
  try:
    main()
  except Exception as e:
    print(e)
    