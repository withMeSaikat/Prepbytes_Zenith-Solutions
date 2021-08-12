def addStrings(a, b, len_a, len_b):
    # Length of a is greater than b
    res = ""
    rem = 0

    for i in range(len(b)):
        s = int(a[len_a - i - 1]) + int(b[len_b - i - 1]) + rem
        res = str(s % 10) + res
        rem = s // 10

    k = len_a - len_b - 1

    while k >= 0:
        s = int(a[k]) + rem
        res = str(s % 10) + res
        rem = s // 10
        k -= 1

    if k < 0 and rem > 0:
        res = str(rem) + res

    return res


# print(addStrings('999999', '9999'))

def main():
    for _ in range(int(input())):
        n = int(input())
        arr = input().split()

        for i in range(1, n):
            len_curr = len(arr[i])
            len_prev = len(arr[i-1])

            if len_curr > len_prev:
                arr[i] = addStrings(arr[i], arr[i-1], len_curr, len_prev)
            else:
                arr[i] = addStrings(arr[i-1], arr[i], len_prev, len_curr)

        print(arr[-1])

if __name__ == '__main__':
    main()