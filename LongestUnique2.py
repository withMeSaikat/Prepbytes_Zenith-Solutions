def solution(s, n):
    counts = [0] * n
    visitedIndex = [-1] * 128 
    prevIndex = 0
    i = 0

    while i < n:
        visitedIndex[ord(s[i])] = i
        
        if i == 0:
            j = 1
            counts[0] = 1
        else:
            j = prevIndex + counts[prevIndex]
            counts[i] = j - i
        
        if i >= j:
            j = i + 1
            counts[i] = 1

        #print("i:", i, " j:", j)
        while(j < n):
            prevIndOfCurChar = visitedIndex[ord(s[j])]
            if prevIndOfCurChar >= 0 and not prevIndOfCurChar < i:
                prevIndex = i
                i = prevIndOfCurChar
                j = n
                visitedIndex[ord(s[i])] = -1
                continue
            else:
                #print('Counting ', j)
                visitedIndex[ord(s[j])] = j
                counts[i] += 1
            j += 1
            if j == n:
                i = n
        
        i += 1

    print('Count Array: ', counts)
    maxInd = 0
    for i in range(1, n):
        if counts[i] > counts[maxInd]:
            maxInd = i
    
    return counts[maxInd]
# Solved
def main():
    for _ in range(int(input())):
        s = input().strip()
        n = len(s)
        print(solution(s, n))

if __name__ == '__main__':
    main()


# TESTCASES
# 6
# prepbytes
# xyprepbytes
# codingassignment
# aaassaaa
# asasas
# aasasasp
