def bruteForce(l, r):
    count = 0
    for i in range(l, r+1):
        temp = str(i)
        if temp[0] == temp[-1]:
            count += 1
    return count

def findDigitPalindromes(l, r):
    '''
    This function calculates number of digit palindromes between l and r(inclusive)
    l and r have same number of digits
    '''

    # If single digit then r - l + 1 number of possibilites
    if len(str(l)) == 1:
        return r - l + 1

    # Initializing Count variable
    count = 0

    # When lower range < upper range
    while l <= r:

        temp = str(l)
        # print("Current temp:", temp)

        # If the first and ladt digit are same then 
        # Calculating no of numbers having both end same,
        # e.g. if l = 1661 and r = 1770 then 1661, 1671, ..., 1761 are also digit palindromes
        # Number of such numbers = (1770 - 1661 + 1) = 12
        if temp[0] == temp[-1]:
            if len(temp) > 2:
                if int(str(r)[0]) > int(temp[0]):
                    base = int(temp[1:-1])
                    count += ((int(str(r)[0]) - int(temp[0])) * 100 - int(base))
                    temp = str(int(str(r)[0]) - 1) + '0' * (len(temp) - 2) + str(int(str(r)[0]) - 1)
                else:
                    count += (int(str(r)[1:-1]) - int(temp[1:-1]) + 1)
            else:
                count += 1
            
            
            # Incrementing both end digits by 1
            if temp[0] != '9':
                temp = str(int(temp[0]) + 1) + temp[1:]
            else: 
                break
            if temp[-1] != '9':
                temp = temp[0:-1] + str(int(temp[-1]) + 1)
            
        
        # If not same, then replacing the lesser digit to higher digit and vice versa
        elif int(temp[0]) < int(temp[-1]):
           
            temp = temp[-1] + temp[1:]

        else:
            #temp = str(l)
            #temp[-1] = temp[0]
            temp = temp[0:-1] + temp[0]
        
        # Updating l which will be again checked in while loop condition
        l = int(temp)   
        # print("Next temp:", l)
    return count

def mySolution(l, r):
    l_n = len(l)
    r_n = len(r)
    C = 0
    #print("===========")
    # Calculating number of digit palindromes between lowerNumber and maximum same number of digit number
    # e.g. (4, 9), (27, 99), (123, 999), etc.
    if(l_n < r_n):
        C += findDigitPalindromes(int(l), int('9' * l_n))
        l_n += 1
        l = '1' + '0' * (l_n - 1)
    
    # Calculating same upto the point number of digits of lowerNumber is equal to that of UpperNumber 
    while(l_n < r_n):
        C += findDigitPalindromes(int('1' + '0' * (l_n - 1)), int('9' * l_n))
        l_n += 1
        l = '1' + '0' * (l_n - 1)
    
    # Calculating same to upto upperNumber
    C += findDigitPalindromes(int(l), int(r))
    return C

# T = int(input())

# while T > 0:
#     l, r = input().split()
#     #print(l, r)
import random
random.seed(7)
def Test(T):
    while T > 0:
        l = random.randint(1, 10000)
        r = random.randint(1, 10000) + random.randint(1, 1000)

        c_brute_force = bruteForce(int(l), int(r))
        c_sol = mySolution(str(l), str(r))
        if c_sol != c_brute_force:
            print('Sol:', c_sol)
            print('Brute Force:', c_brute_force)
            print("inp:", l, r)
        else:
            print("Passed!")
        T -= 1
    #print("===========")
    #T -= 1
Test(50)