#  Day 1: Roman Numeral Toolkit CLI
# 🎯 Goal:
# Build a simple command-line interface (CLI) tool that:

# Converts integers to Roman numerals

# Converts Roman numerals to integers

# 🧠 Focus:
# Apply your RomanNumerals class

# Accept input from sys.argv or input()

# Add basic error handling (e.g., invalid Roman strings)

# 💡 Bonus:
# Format output nicely

# Log to a text file with conversion history
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
class RomanNumerals:
    @staticmethod
    def to_roman(val: int) :
        result = ""
        
        for symbol, value in roman_numerals.items():
            while(val >= value) :
                result += symbol
                val -= value
        
        return result
    
    @staticmethod
    def to_number(roman: str):
        if (not roman):
            return 0
        if (len(roman) == 1) :
            return roman_numerals[roman]
            
        first = roman_numerals[roman[0]]
        second = roman_numerals[roman[1]]
        
        if first < second:
            return second - first + RomanNumerals.to_number(roman[2:]) 
        else:
            return first + RomanNumerals.to_number(roman[1:])
        
print("Welcome to the Roman Numeral Converter!\nConvert numbers to Roman numerals or Roman numerals to numbers.")
print('You can choose to convert a number to roman or a roman to a number')
question = {
    'to_number': 'convert your roman number back to base 10 number?',
    'to_roman' : 'convert your number to a roman number?'
}

for choice, action in question.items():
    print(f'Do you want to  {action} , choose {choice}')

ans = input("Enter your choice: ")
if ans not in question.keys():
    print("Invalid choice. Please enter 'to_number' or 'to_roman'.")
    exit()
print(f'You have chosen to {question[ans]}')
print("Please enter your value:")
value = input()
if all(char in roman_numerals for char in value):
    final_ans = RomanNumerals.to_number(str(value))
    with open("conversion_history.txt", "a") as file:

        file.write(f'Conversion Result: Roman numeral "{value}" equals {final_ans} in base 10.\n')
    print(f'Conversion Result: Roman numeral "{value}" equals {final_ans} in base 10.')
else:
    try:
        value = int(value)
        if value <= 0:
            print(f'Conversion Result: Number "{value} is not possible since value is less than 0".')
        else:
            final_ans = RomanNumerals.to_roman(value)
            with open("conversion_history.txt", "a") as file:
                file.write(f'Conversion Result: Number "{value}" equals "{final_ans}" in Roman numeral.\n')
            print(f'Your number of {value} to roman is {final_ans}')
    except ValueError:
            print("Invalid input. Please enter a valid integer.")