def findMaxMin(arr, flag=False):
    max = min = 0

    for i in range(1):
        for j in range(i + 1, len(arr)):
            current_sum = 0
            max_sum = 0

            if flag:
                current_sum = arr[j] - j
                max_sum = arr[max] - max
                min_sum = arr[min] - min
            else:
                current_sum = arr[j] + j
                max_sum = arr[max] + max
                min_sum = arr[min] + min

            if current_sum > max_sum:
                max = j
            
            if current_sum < min_sum:
                min = j

    res = 0
    if flag:
        # max *= -1
        # min *= -1
        res = (arr[max] - max) - (arr[min] - min)
    else:
        res = (arr[max] + max) - (arr[min] + min)

    return (res, (max, min))


# T  = int(input())


# while T > 0:
#   n = int(input())
#   arr = list(map(int, input().split()))
#   T -= 1
  # Ak + k
def Solution(arr):
    res1, indices1 = findMaxMin(arr)
    res2, indices2 = findMaxMin(arr, True)
    if res1 > res2:
        return (res1, indices1)
    else:
        return (res2, indices2)

    # res = max(res1, res2, -1 * res1, -1 * res2)
    # return res
  
import random
random.seed(7)


def BruteForce(arr):
    diff = None
    indices = None
    for i in range(len(arr)):
        for j in range(i, len(arr)):
            if not diff and diff != 0:
                diff = abs(arr[i] - arr[j]) + abs(i - j)
            curr = abs(arr[i] - arr[j]) + abs(i - j)
            if curr > diff:
                diff = curr
                indices = (i, j)
    return (diff, indices)

def Test(n):
    while n > 0:
        m = random.randint(1, 20)
        arr = [random.randint(0, 100) for i in range(m)]
        res1, indices1 = BruteForce(arr)
        res2, indices2 = Solution(arr)
        if res1 != res2:
            print("BruteForce ans:", res1, "Indices: ", indices1)
            print("Solution Ans:", res2, "Indices: ", indices2)
            print("ARR:", arr)
        else:
            print("TEST CASE PASSED")
        n -= 1

Test(20)