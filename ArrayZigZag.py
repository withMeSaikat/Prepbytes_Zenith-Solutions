def Solution3(arr, n, ind):
    oddCount = evenCount = 0
    count = 0
    # For maximizing even-indexed elements
    for i in range(ind, n, 2):
        temp = 0
        if i > 0 and arr[i] < arr[i-1]:
            temp = max(temp, arr[i-1] - arr[i] + 1)
        if i < n - 1 and arr[i] < arr[i+1]:
            temp = max(temp, arr[i+1] - arr[i] + 1)
        count += temp
    return count
        
def Solution2(arr, n):
    countIn = [0] * n
    countDec = [0] * n
    totalIn = totalDec = 0

    for i in range(n):
        if i != 0:
            if arr[i] < arr[i-1]:
                countIn[i] = max(countIn[i], arr[i-1] - arr[i] + 1)
            else:
                countDec[i] = max(countDec[i], arr[i] - arr[i-1] + 1)
        if i != n-1:
            if arr[i] < arr[i+1]:
                countIn[i] = max(countIn[i], arr[i+1] - arr[i] + 1)
            else:
                countDec[i] = max(countDec[i], arr[i] - arr[i+1] + 1)
        
        totalIn += countIn[i]
        totalDec += countDec[i]

    # print("Input   Array: ", arr)
    # print("CountIn Array: ", countIn)
    # print("CountDe Array: ", countDec)

    oddCountIn = 0
    oddCountDec = 0
    for i in range(1, n, 2):
        oddCountIn += countIn[i]
        oddCountDec += countDec[i]
    
    return min(oddCountIn, totalIn - oddCountIn, oddCountDec, totalDec - oddCountDec)

def Solution1(arr, n):
    arr.insert(0, 0)
    arr.append(0)

    oddCount = 0
    evenCount = 0

    for i in range(1, n+1):
        count = 0
        if arr[i] < arr[i - 1]:
            count = max(count, arr[i-1] - arr[i] + 1)
        if arr[i] < arr[i+1]:
            count = max(count, arr[i+1] - arr[i] + 1)
        
        if (i - 1) % 2 == 0:
            evenCount += count
        else:
            oddCount += count
    #print(arr[i], "-->", "even: ", evenCount, ' odd:', oddCount)
    return min(oddCount, evenCount)

def main():
    n = int(input())
    arr = list(map(int, input().strip().split(' ')))
    # res = Solution2(arr, n)
    res = min(Solution3(arr, n, 0), Solution3(arr, n, 1))
    print(res)

if __name__ == '__main__':
    main()
    