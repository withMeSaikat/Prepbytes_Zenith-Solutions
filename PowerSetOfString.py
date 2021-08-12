def getPowerSet(s, index):
    if index == len(s) - 1:
        res = []
        res.append(s[index])
        return res

    arr = getPowerSet(s, index+1)
    curr_char = s[index]

    for i in range(len(arr)):
        arr.append(curr_char + arr[i])

    arr.append(curr_char)
    return arr


def main():
    s = list(input())
    s.sort()

    arr = getPowerSet(s, 0)
    for i in range(len(arr) - 1, -1, -1):
        print(arr[i])
    #print("Length of powerset:", len(arr))


# Solved
if __name__ == '__main__':
    main()
