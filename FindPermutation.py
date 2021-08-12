def getPermutation(inp, string, perms, counts, m):
    if len(perms) == m:
        print(perms[-1])
        return 0

    if counts == 0:
        perms.append(string[:-1])
        return 1

    for i in range(len(inp)):
        # if i == index:
        #   continue

        res = getPermutation(inp[:i] + inp[i+1:],
                             string + inp[i] + ' ', perms, counts - 1, m)
        if res == 0:
            return 0

    return 1

def getPermutations2(inp):
    if len(inp) == 0:
        return []
    
    if len(inp) == 1:
        return inp
    
    for i in range(len(inp)):
        l = []
        curr = str(inp[i])
        inp1 = inp[:i] + inp[i+1:]

        for p in getPermutations2(inp1):
            l.append(p + curr)
    return l

def main():
    n, m = map(int, input().split())
    inp = input().split()

    perms = []
    # res = getPermutation(inp, "", perms, n, m)

    # print("All permutations: ", perms)
    # print("Answer: ", perms[-1])
    arr = getPermutations2(inp)
    print(arr)

if __name__ == '__main__':
    main()
