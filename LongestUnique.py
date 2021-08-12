def solution(s, n):
    counts = [0] * n
    visitedIndex = [-1] * 128 


    for i in range(n):
        visitedIndex[ord(s[i])] = i
        
        if i == 0:
            j = 1
            counts[0] = 1
        else:
            j = i + counts[i - 1] - 1
            counts[i] = counts[i - 1] - 1
        
        if i >= j:
            j = i + 1
            counts[i] = 1

        while(j < n):
            if visitedIndex[ord(s[j])] >= 0 and not visitedIndex[ord(s[j])] < i:
                j = n
                visitedIndex[ord(s[i])] = -1
            else:
                visitedIndex[ord(s[j])] = j
                counts[i] += 1
            j += 1
    print('Count Array: ', counts)
    maxInd = 0
    for i in range(1, n):
        if counts[i] > counts[maxInd]:
            maxInd = i
    
    return counts[maxInd]

# Solved(Not Sure -- Giving TLE)
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
