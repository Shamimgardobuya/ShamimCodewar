roman_numerals = {
        "M": 1000,
        "CM": 900,
        "D": 500,
        "CD": 400,
        "C": 100,
        "XC": 90,
        "L": 50,
        "XL": 40,
        "X": 10,
        "IX": 9,
        "V": 5,
        "IV": 4,
        "I": 1
    }


def to_roman(val : int) -> str:  #works but not sustainable
    val = list(map(int, str(val)))
    val.reverse()
    my_dict = {}
    for index, element in enumerate(val):
        
        new_value = (10 ** index) * element
        base = (10 ** index)

        if new_value == 0:
            continue
        elif(new_value in roman_numerals.values() or new_value and base in roman_numerals.values()):
            for key, value in roman_numerals.items():
                if new_value == value:
                    my_dict[new_value] = key

                elif base == value and new_value not in my_dict: 
                    my_dict[new_value] = key  * element      

    my_dict = dict(sorted(my_dict.items(), reverse=True))
    return ''.join(my_dict.values())
# #using greedy algorithm:
#  Example: to_roman(1987)
#what the loop does step-by-step:

# 1987 ≥ 1000 → add "M" → val = 987

# 987 ≥ 900 → add "CM" → val = 87

# 87 ≥ 50 → add "L" → val = 37

# 37 ≥ 10 → add "X" → val = 27

# 27 ≥ 10 → add "X" → val = 17

# 17 ≥ 10 → add "X" → val = 7

# 7 ≥ 5 → add "V" → val = 2

# 2 ≥ 1 → add "I" → val = 1

# 1 ≥ 1 → add "I" → val = 0
# Start from the top (largest value, "M" = 1000).

# Ask: Can I subtract this from my number?

# If yes → subtract it and add the symbol.

# Repeat until the number becomes zero.
def to_roman(val: int) :
    result = ""
    for symbol, value in roman_numerals.items():
        while(val >= value) :
            result += symbol
            val -= value
            
    return result

# print(to_roman(MMMCCXLIX)) 
# print(list(roman_numerals.keys()).index('X'))
#binary won't be possible since we don't have a target making the binary continue forever
# def to_number(roman: str):
#     ans = 0
#     roman =  list(roman)
    
#     low, high = 0, len(roman) -1 
#     # return low , high
#     while (low <= high) :
#         mid = low + (high - low) // 2
#         print( roman[mid])
#         if (roman[mid] in roman_numerals):
#             ans += roman_numerals[roman[mid]]
#             print(ans)
        
#         elif(mid < list(roman_numerals.keys()).index(roman[mid])):
#             print(roman[mid])
#             ans = mid
#             low = mid + 1
#         else:
#             print(roman[mid])

#             high = mid - 1
#     return ans
    
def to_number(roman:str) :  #not utilizing recursion fully and mostly works for romans that are already in the dictionary 
    if (roman in roman_numerals):
        return roman_numerals[roman]
    # roman =  list(roman)
    ans = 0

    for i in roman:
        if i in roman_numerals:
            ans += roman_numerals[i]
        else:
            to_number(i)
    return ans
#better way to utilize recursion
def to_number_by_recursion(roman: str) :
    #base case
    # if (roman in roman_numerals):
    #     return roman_numerals[roman]
    if (not roman) :
        return 0
    #another base case
    if (len(roman) == 1):
        print(roman)
        return roman_numerals[roman]
        
    first = roman_numerals[roman[0]]
    second  = roman_numerals[roman[1]]
    
    if (first < second) :
        return second - first + to_number_by_recursion(roman[2:])
    else:
        return first + to_number_by_recursion(roman[1:])


print(to_number_by_recursion("VI"))

#fully utilizing Recursion
# 
    
    
        


    # @staticmethod
    # def from_roman(roman_num : str) -> int:
    #     return 0
    
#binary ish for fun
# Summary of Logic:
# If a 2-letter Roman pair exists in the dictionary, consume it.

# Else, use the single-letter Roman value.

# Continue until the end.

#NB: ROMAN NUMERALS HIERACHY starts from left as bigger than right, if you see right being more than left, take the right value and subtract from the left value e.g IV = 5 -1 = 4 
def roman_to_int(roman: str) -> int:
    roman_numerals = {
        "M": 1000,
        "CM": 900,
        "D": 500,
        "CD": 400,
        "C": 100,
        "XC": 90,
        "L": 50,
        "XL": 40,
        "X": 10,
        "IX": 9,
        "V": 5,
        "IV": 4,
        "I": 1
    }

    i = 0
    total = 0

    while i < len(roman):
        # Look ahead for 2-character match like 'CM', 'IX', etc.
        if i + 1 < len(roman) and roman[i:i+2] in roman_numerals:
            total += roman_numerals[roman[i:i+2]]
            i += 2
        else:
            total += roman_numerals[roman[i]]
            i += 1

    return total
