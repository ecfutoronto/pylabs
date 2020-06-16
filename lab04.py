'''
adding random comments
'''

def caesar(plainText, shift): 

    for ch in plainText:
        if ch.isalpha():
            stayInAlphabet = ord(ch) + shift 
            if stayInAlphabet > ord('z'):
                stayInAlphabet -= 26
            finalLetter = chr(stayInAlphabet)
        cipherText = ""
        cipherText += finalLetter

    print "Your ciphertext is: ", cipherText

    return cipherText


def above_average(elems):
    average = sum(elems) / len(elems)

    return len([x for x in elems if x > average])

def falling_power(n, k):
    prod = 1
    m = n - k + 1
    # No base case required m > n if k = 0
    # and m = n if k = 1 for any n 
    while n >= m:
        prod = prod * n
        n = n - 1
    return prod

def forward_difference(elems):
    fwd_diff = []
    # Base case
    if len(elems) == 1:
        return fwd_diff
    
    for e in range(len(elems) - 1):
        fwd_diff.append(elems[e+1]-elems[e])

    return fwd_diff

def shift_characters(text):
    ch = ''
    # ord returns the Unicode codepoint
    # chr returns the char
    for char in list(text):
        ch += chr(ord(char)+1)
    return ch

def alternating_sign_sum(numbers):
    # Get the indicies at the odd position, sum them
    # Get the indicies at the even positions, sum them
    # Take the difference
    return sum(numbers[0::2]) - sum(numbers[1::2])
    
def parity_partition(numbers):
    return list(filter(lambda x : (x % 2 == 0), numbers)) + list(filter(lambda x : (x % 2 != 0), numbers))

def extract_antidiagonal(matrix):
    ad = []
    n = len(matrix)
    for w in range(n):
        for x in range(n):
            if w != x and  w + x == n - 1:
                ad.append(matrix[w][x])
    return ad

def dominates(first, second):
    dominate = list(map(lambda x, y: x >= y, first, second))
    # if False in dominate:
    return False if False in dominate else True

if __name__ == "__main__":
    # Test cases
    print(above_average([1,2,3,4,5]))
    print(falling_power(8, 3))
    print(falling_power(10, 5))
    print(falling_power(-4, 5))
    print(falling_power(4, 0))
    print(forward_difference([4, 2, 7, 1, 8, 3]))
    print(forward_difference(forward_difference([4, 2, 7, 1, 8, 3])))
    print(shift_characters('Hello world'))
    print(alternating_sign_sum([3, 5, 2, 4, 8, 2]))
    print(extract_antidiagonal([[7, 5, 2, 9], [1, -3, 6, 2], [7, 4, 4, 1], [3, 9, 0, 2]]))
    print(dominates([6, 10, 2, 4], [5, 10, 1, 5, 6] ))