def sumOfSubsets(arr, n, ind, res):
    if ind == n-1:
        res.append(arr[ind])
        return arr[ind]
    
    s = sumOfSubsets(arr, n, ind + 1, res)
    for i in range(len(res)):
        res.append(res[i] + arr[ind])
        s += res[-1]
    
    s += arr[ind]
    res.append(arr[ind])

    return s

def main():
    for _ in range(int(input())):
        n = int(input())
        arr = list(map(int, input().strip().split()))
        s = sumOfSubsets(arr, n, 0, [])
        print(s)

# Solved    
if __name__ == '__main__':
    main()