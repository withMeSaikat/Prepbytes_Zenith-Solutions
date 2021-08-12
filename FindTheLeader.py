def mySolution(arr, n):
    res = ""
    lastMax = n - 1

    for i in range(n-1, -1, -1):
        if arr[i] >= arr[lastMax]:
            #res.append(arr[i])
            res = str(arr[i]) + res
            lastMax = i

    # for num in res:
    #     print(num, end=' ')
    # print()
    return res

# for _ in range(int(input())):
#   n = int(input())
#   arr = list(map(int, input().split(' ')))
def demoSol(arr, n):
    res = ''
    for i in range(n):
        flag = True
        for j in range(i+1, n):
            if arr[i] < arr[j]:
                flag = False
        if flag:
            res += str(arr[i])
    return res

import random

def Test():
    T = random.randint(6, 100)
    for _ in range(T):
        n = random.randint(1, 10000)
        arr = [random.randint(0, 10000) for i in range(n)]
        sol1 = demoSol(arr, n)
        sol2 = mySolution(arr, n)

        if sol1 != sol2:
            print(sol1)
            print(sol2)
            print("Array:", arr)
            break
        else:
            print('Passed!')
Test()