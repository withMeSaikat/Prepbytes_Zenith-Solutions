def findNum(evenSum, oddSum, string, n):
    isOddPos = n % 2 == 0
    if n == 1:
        if isOddPos and evenSum >= oddSum and evenSum - oddSum <= 9:
            string += str(evenSum - oddSum)
            print(string, end=' ')
        elif (not isOddPos) and oddSum >= evenSum and oddSum - evenSum <= 9:
            string += str(oddSum - evenSum)
            print(string, end=' ')
        return


    for i in range(0, 10):
        if string == '' and i == 0:
            continue

        if isOddPos:
            findNum(evenSum, oddSum + i, string + str(i), n - 1)
        else:
            findNum(evenSum + i, oddSum, string + str(i), n - 1)


def main():
    n = int(input())

    arr = []
    findNum(0, 0, "", n)
    # print(arr)

# SOLVED
if __name__ == '__main__':
    main()
