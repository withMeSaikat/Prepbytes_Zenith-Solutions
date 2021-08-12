def rotate(arr,ind, n):
  left = ind
  right = n
  
  while(right > left):
    # arr[left], arr[right] = arr[right], arr[left]
    temp = arr[left]
    arr[left] = arr[right]
    arr[right] = temp
    right -= 1
    left += 1
  

# if __name__ == '__main__':
for _ in range(int(input())):
  n, k = map(int, input().split(' '))
  print(n, k)
  arr = list(map(int, input().strip().split(' ')))[:n]
  print("Array:", arr)
  k = k % n
  if k > 0:
    rotate(arr, n - k, n - 1)
    rotate(arr, 0, n - k - 1)
    rotate(arr, 0, n - 1)
  for num in arr:
    print(num, end=' ')
  print()


  