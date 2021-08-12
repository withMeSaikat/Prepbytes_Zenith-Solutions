def Solution3(arr, n):
    arr = list([(arr[i], i) for i in range(n)])
    arr.sort(key=lambda elem: elem[0])

    print("Arr:", arr)
    minInd = 0
    maxInd = 1

    for i in range(n):
        curr = arr[i][-1]

        tempMax = maxInd
        tempMin = minInd

        if curr > arr[maxInd][-1]:
            tempMax = maxInd
        if curr < arr[minInd][-1]:
            tempMin = minInd
        
        if tempMax > tempMin or tempMax > minInd:
            maxInd = tempMax
        if tempMin < tempMax or tempMin < maxInd:
            minInd = tempMin
    
    print(maxInd, minInd)
def Solution1(arr, n):
    maxDiff = -1
    for i in range(n-1, 0, -1):
        if arr[i] > arr[0]:
            maxDiff = i

    prev = 0
    maxInd = maxDiff

    for j in range(1, n):
        if arr[j] >= arr[prev]:
            continue
        
        if maxInd != -1:
            for k in range(maxInd + 1, n):
                if arr[k] > arr[j] and k - j > maxDiff:
                    maxDiff = k - j
                    prev = j
                    maxInd = k

    return maxDiff

def Solution2(arr, n):
    ind = list([(arr[i], i) for i in range(n)])
    ind.sort(key= lambda elem: elem[0])

    maxDiff = -1
    start = 0
    end = -1
    
def main():
    n = int(input())
    arr = list(map(int, input().split()))
    # res = Solution1(arr, n)
    # print(res)
    Solution3(arr, n)

# def Test():

if __name__ == '__main__':
    main()
  