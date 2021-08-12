def Solution(s, t):
    if len(t) > len(s):
        return False

    i = j = 0

    while(i < len(t)):
        if s[j] != t[i]:
            if t[i] == '-':
                return False
            
            if j + 1 < len(s) and s[j + 1] == '-':
                i += 1
                j += 2
                continue
            else:
                return False
        i += 1
        j += 1

    if j <= len(s) - 1:
        return False

    return True


def main():
    for _ in range(int(input())):
        s = input()
        t = input()
        if Solution(s, t):
            print('YES')
        else:
            print('NO')

# Solved
if __name__ == '__main__':
    main()
