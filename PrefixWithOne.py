def prefixWithOne(arr, n, ind, noOfOnes, noOfZeroes):
    if ind == n:
        if noOfOnes >= noOfZeroes:
            for i in range(n):
                print(arr[i], end='')
            print(" ", end='')
        return

    arr[ind] = 1
    prefixWithOne(arr, n, ind + 1, noOfOnes + 1, noOfZeroes)

    if noOfZeroes + 1 <= noOfOnes:
        arr[ind] = 0
        prefixWithOne(arr, n, ind + 1, noOfOnes, noOfZeroes + 1)

    return

def main():
    for _ in range(int(input())):
        n = int(input())
        arr = [-1] * n
        prefixWithOne(arr, n, 0, 0, 0)
        print()

if __name__ == '__main__':
    main()