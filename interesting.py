# Is n interesting → return 2

# Is n+1 or n+2 interesting → return 1

def actual_interesting(number, awesome_phrases):
    numb = list(map(int, str(number)))
    incr = [i for i in range(numb[0], len(numb) + 1)]
    decr = [i for i in range(numb[0], len(numb) + 1, - 1)]
    reversed = numb[::-1]
    # range(6,6) //item cannot exceed 6 we neeed better approach
    print('incr', range(numb[0], len(numb) + 1))
    _list = [ number in awesome_phrases, reversed == numb , numb.count(numb[0]) == len(numb)]
    if (True in _list) :
        return 2
    else:
        if numb.count(numb[0]) > 0 and numb.count(numb[0]) == 1 and numb.count(0) == len(numb) - 1 :
            return 2
        elif incr == numb or decr == numb  :  #increamenting or decreamenting
            return 2
        
    return 0

def is_interesting(number, awesome_phrases):
    
    for offset in [0, 1 , 1]: 
        number += offset
        if ( number < 100):
            continue
        elif( actual_interesting(number, awesome_phrases) == 2 and offset == 0):
            return 2 
        elif( actual_interesting(number, awesome_phrases) == 2 and offset > 0):
            return 1
    return 0


# Test cases
print(is_interesting(67890, [1337, 256]), "Expected: 2")
