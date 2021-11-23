def binSearchUpper(arr, n, key):
    low = 0
    up = n
    while up > low:
        mid = low + (up - low) // 2
        if arr[mid] > key:
            low = mid
        else:
            up = mid - 1
    return n - up - 1

def main():
    # for _ in range(int(input())):
    n = int(input())
    arr = list(map(int, input().strip().split()))
    arr.sort(reverse=True)
    q = int(input())
    for k in range(q):
        x = int(input())
        ind = binSearchUpper(arr, n, x)
        print(ind)

#Solved
if __name__ == '__main__':
    main()