n = int(input())

arr = list(map(int, input().split()))

prevOp = 0
magic = [0] * n
count = 0

for i in range(n):
    magic[i] += prevOp
    count += abs(arr[i] - magic[i])
    prevOp += (arr[i] - magic[i])
    #print(magic, count)

print(count)

