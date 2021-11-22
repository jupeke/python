'''
A palindromic number reads the same both ways. The largest palindrome
made from the product of two 2-digit numbers is 9009 = 91 × 99.
Find the largest palindrome made from the product of two 3-digit numbers.
'''
import math
def is_palindrome(number):
    is_pal = True
    numb_str = str(number)
    size = len(numb_str)
    half_size = math.floor(size/2) # The eventual middle element does not matter.
    for i in range(half_size):
        if(numb_str[i] != numb_str[-(i+1)]):
            is_pal = False
            break
    return is_pal

# Returns a list with three elements: the two factors of the
# largest palindrome and the result itself.
def find_largest_palindrome(numb_of_digits):
    max = (10 ** numb_of_digits)-1
    a = 1
    b = 1
    largest = 1
    # i starts at 0, that's why 1 is added to the
    for i in range(max):
        for k in range(max):
            if is_palindrome((i+1)*(k+1)) and (i+1)*(k+1) > largest:
                largest = (i+1)*(k+1)
                a = i+1
                b = k+1
    return [a, b, largest]

# Main
result = find_largest_palindrome(3)
print("{} times {} = {}".format(result[0],result[1],result[2]))
