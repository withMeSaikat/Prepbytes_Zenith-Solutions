def addStrings(a, b):
    # Length of a is >= length of b

    len_a = len(a)
    len_b = len(b)

    res = ''
    carry = 0
    for i in range(len_b):
        s = int(a[len_a - i - 1]) + int(b[len_b - i - 1]) + carry
        res = str(s % 10) + res
        carry = s // 10

    k = len_a - len_b - 1

    while k >= 0:
        s = int(a[k]) + carry
        res = str(s % 10) + res
        carry = s // 10
        k -= 1
    
    if carry != 0:
        res = str(carry) + res
    
    return res

def singleDigitMult(m, n):
    # n is single digit
    # m is string

    carry = 0
    res = ''
    for i in range(len(m) - 1, -1, -1):
        mul = int(m[i]) * n + carry
        res = str(mul % 10) + res
        carry = mul // 10

    if carry != 0:
        res = str(carry) + res

    return res

def multiDigitMul(s1, s2):
    res = '0'
    len_s2 = len(s2)

    for i in range(len_s2):
        m = singleDigitMult(s1, int(s2[len_s2 - i - 1]) * (10 ** i))
        res = addStrings(m, res)

    return res

def main():
    for _ in range(int(input())):
        s1, s2 = input().strip().split()
        print(multiDigitMul(s1, s2))

# Solved
if __name__ == '__main__':
    main()