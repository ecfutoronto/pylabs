import primes

''' Checks if some text is a palindrome '''
def is_palindrome(text):
    
    if text[::-1].lower() == text.lower():
        return True
    return False

''' Checks if some number is a palindrome '''
def palindromic_primes(start, end):
    lst = []

    for x in range(start, end+1):
        if primes.is_prime(x):
            if str(x)[::-1] == str(x):
                lst.append(x)

    return lst

''' Question 2: Primes where if the number read backword from right to left are 
another prime number and are not palindromic primes '''
def emirp_primes(start, end):
    lst = []

    for x in range(start, end+1):
        if primes.is_prime(x):
            if primes.is_prime(int(str(x)[::-1])) and str(x)[::-1] != str(x):
                lst.append(x)

    return lst

''' Question 3: Primes are of the form j and j+2 where j and j+2 are prime '''
def twin_primes(start, end):
    lst = []

    for x in range(start, end+1):
        if primes.is_prime(x) and primes.__is_prime(x+2):
            lst.append(tuple([x,x+2]))

    return lst

''' Question 4: Primes are of the form 2j+1 where j is also a prime'''
def safe_primes(n):
    lst = []
    j = 1

    while len(lst) < n:
        if primes.is_prime(j) and primes.__is_prime(2*j+1):
            lst.append(2*j+1)
        j = j + 1
    
    return lst

''' Question 5: Prime numbers where the mathematical average of a prime number
and the next prime number is less than the next next prime number '''
def strong_primes(n):
    lst = []
    ''' We can only start at k1 which is 3. 
    The formula is K_n = 1/2 ( K_(n-1) + K_(n+1) ) '''
    
    j = 3
    idx = 1
    while len(lst) < n:
        if primes.is_prime(j):
            j1 = primes.kth_prime(idx-1)
            j2 = primes.kth_prime(idx+1)
            if (j1+j2)/2 < j:
                lst.append(j)
            idx = idx + 1
        j = j + 1
    return lst

''' Test cases '''
if __name__ == "__main__":
    print(primes.is_prime(5))
    print(primes.kth_prime(0))
    print(primes.kth_prime(2))
    print(palindromic_primes(1,1000))
    print(emirp_primes(1,1000))
    print(twin_primes(1,150))
    print(safe_primes(21))
    print(strong_primes(21))