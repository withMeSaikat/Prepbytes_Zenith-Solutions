import math


def binSearchLower(arr, key):
    low = 0
    up = len(arr)
    while up > low:
        mid = low + (up - low) // 2
        if arr[mid] >= key:
            up = mid
        else:
            low = mid + 1

    return low


def binSearchUpper(arr, key):
    low = 0
    up = len(arr)
    while up > low:
        mid = low + (up - low) // 2
        if arr[mid] > key:
            up = mid
        else:
            low = mid + 1

    return low


def getCommonDivisors(a, b):
    if a > b:
        return getCommonDivisors(b, a)

    arr = [0] * a
    i = 1
    l = 0
    r = a - 1
    while i <= int(math.sqrt(a)):
        # print("Checking", i)
        if a % i == 0 and b % i == 0 and i <= a // i:
            arr[l] = i
            l += 1
        else:
            i += 1
            continue

        j = a // i
        if i < j and b % j == 0:
            arr[r] = j
            r -= 1

        i += 1

    res = arr[:l] + arr[r+1:]
    return res

# try:
#   print(getCommonDivisors(121, 121))
# except Exception as e:
#   print(e)


def main():
    a, b = map(int, input().split())
    q = int(input())

    divisors = getCommonDivisors(a, b)

    for i in range(q):
        low, high = map(int, input().split())
        # lowInd = binSearchLower(divisors, low)
        highInd = binSearchUpper(divisors, high)
        # print("Ans: ")
        # for k in range(lowInd, highInd):
        #     print(divisors[k], end=' ')
        # print()
        if highInd != 0 and divisors[highInd - 1] >= low:
            print(divisors[highInd - 1])
        else:
            print(-1)

if __name__ == '__main__':
    main()
# arr = [1, 2, 3, 3, 3, 5, 6]
# print(binSearchLower(arr, 3))
# print(binSearchLower(arr, 4))
# print(binSearchUpper(arr, 3))
# print(binSearchUpper(arr, 4))
# print(binSearchUpper(arr, 5))
