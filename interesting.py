# Is n interesting → return 2

# Is n+1 or n+2 interesting → return 1

def actual_interesting(number, awesome_phrases):
    numb = list(map(int, str(number)))
    incr = "01234567890"
    decr = "9876543210"
    reversed = numb[::-1]
    numb_str = ''.join(map(str, numb))
    _list = [ number in awesome_phrases, reversed == numb , numb.count(numb[0]) == len(numb)]
    if (True in _list) :
        return 2
    else:
        if numb.count(numb[0]) > 0 and numb.count(numb[0]) == 1 and numb.count(0) == len(numb) - 1 :
            return 2
        elif numb_str in incr or numb_str in decr  :  
            return 2
        
    return 0

def is_interesting(number, awesome_phrases):
    original_number = number
    for offset in [0, 1 , 1]: 
        number = offset + number
        if ( number < 100):
            continue
        elif( actual_interesting(number, awesome_phrases) == 2 and offset == 0):
            return 2 
        elif( actual_interesting(number, awesome_phrases) == 2 and offset > 0):
            return 1
    return 0

#refactored code
def is_all_same_digits(n):
    digits = str(n)
    return all(d == digits[0] for d in digits)

def is_followed_by_zeros(n):
    s = str(n)
    return s[0] != '0' and set(s[1:]) == {'0'}

def is_sequential_increment(n):
    return str(n) in "1234567890"

def is_sequential_decrement(n):
    return str(n) in "9876543210"

def is_palindrome(n):
    s = str(n)
    return s == s[::-1]

def is_awesome_phrase(n, awesome_phrases):
    return n in awesome_phrases

def actual_interesting(n, awesome_phrases):
    return (
        is_followed_by_zeros(n) or
        is_all_same_digits(n) or
        is_sequential_increment(n) or
        is_sequential_decrement(n) or
        is_palindrome(n) or
        is_awesome_phrase(n, awesome_phrases)
    )

def is_interesting(number, awesome_phrases):
    for i in range(3):
        current = number + i
        if current < 100:
            continue
        if actual_interesting(current, awesome_phrases):
            return 2 if i == 0 else 1
    return 0
