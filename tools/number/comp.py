"""
1 creating a funtion that returns the sum of the 
digits, for example "123" will return "6" 

2 creating a funtion that checks if a number is a 
palindrome for example "1221", "3003" and returns True of False
"""
def sum_of_digits(sumNumber):
    digits_array = [int(digit) for digit in str(sumNumber)]      #turn the number to a string, run over it with a loop and store an array of digits
    return sum(digits_array)                                     #returns the sum of the array, example: [1,2,3] → 6

def isPal(palNumber):
    return str(palNumber)[::-1] == str(palNumber)                #i turn the number to a string, if the string is the same normal and reversed it returns True if not its False