def findNum(s, string, n):
    if n == 1:
        if s <= 9:
            string += str(s)
            print(string, end=' ')
        return
    
    if s > n * 9:
        return

    for i in range(0, 10):
        if string == '' and i == 0:
            continue

        if s - i >= 0:
            findNum(s - i, string + str(i), n - 1)

def main():
    n, s = map(int, input().split())

    arr = []
    findNum(s, "", n)
    # print(arr)

# SOLVED
if __name__ == '__main__':
    main()
