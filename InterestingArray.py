def Solution2(arr, n, k):
    ind = [-1] * (arr[-1] + 1)
    res = None

    for i in range(n):
        if ind[arr[i]] == -1:
            ind[arr[i]] = [i]
        else:
            ind[arr[i]].append(i)

    print("Index Array:", ind)
    for i in range(n):
        num = k - arr[i]
        if num <= arr[-1] and ind[num] != -1 and i < ind[num][-1]:
            j = ind[num][-1]
            print("-->(", i, j, ")")
            if not res:
                res = (i, j)
            if res[-1] < j or (res[-1] == j and res[0] > i):
                res = (i, j)

    return res

def SolutionThree(arr, n, k):
    start = 0
    end = n - 1
    while(start < end):
        if arr[start] + arr[end] == k:
            return (start, end)
        elif arr[start] + arr[end] < k:
            start += 1
        else:
            end -= 1
    return None

def search(arr, key, left, right):
    i = left
    while i <= right:
        mid = left + ((right - left + 1) // 2)
        if arr[mid] == key:
            return mid
        if arr[mid] > key:
            right = mid - 1
        if arr[mid] < key:
            i = mid
        i += 1
    return -1

def Solution1(arr, n, k):
    res = []

    for i in range(n):
        if arr[i] != -1:
            num = k - arr[i]
            if k < arr[i]:
                continue
            j = search(arr, num, i+1, n - 1)
            if j > i:
                res.append((i, j))
                arr[j] = -1
            arr[i] = -1
    if len(res) > 1:
        res.sort(key=lambda elem:elem[1])
    
    res = res[-1]
    return res


for _ in range(int(input())):
    n = int(input())
    arr = list(map(int, input().strip().split(' ')))
    k = int(input())

    res = Solution2(arr, n, k)
    if res:
        print(res[0], res[-1])
    else:
        print('no answer')
    
    