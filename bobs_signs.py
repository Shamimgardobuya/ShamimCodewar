# Define a function estimate(add_cost, remove_cost, old_sign, new_sign) 
# minimum_cost that is adaptable to changes in the market, and can help Bob estimate prices quickly.

# The first 2 arguments are the costs of doing an operation, of adding
# and removing a letter respectively.
# The last 2 arguments are the old sign of the customer, and their request.

# It should return the cost of changing the sign from 
# the old message to the new message. If there are multiple ways 
# to change the sign, it should return the cheapest way

#my solution passed 4 tests but did not pass some of them


from collections import Counter


def estimate(add_cost, remove_cost, old_sign, new_sign):
    # Have fun!
    #loop first through the new string
    #check if character is not in the new sign
    #if it isn't then
    
    if ( len(old_sign)  > 0 and len(new_sign) > 0) :
        letters_to_add = list(set(new_sign) - set(old_sign))
        letters_to_remove = list(set(old_sign) - set(new_sign))

        total_remove_cost = remove_cost * len(letters_to_remove)
        total_additional_cost = add_cost * len(letters_to_add)
        first = ''
        second = ''
        #return key as the extra character
        for key,val in Counter(old_sign).items():
            if val > 1 :
                first += key
            # print(key,val)
        for key,val in Counter(new_sign).items():
            if val > 1 :
                second += key
            # print(key,val)
        
        if len(first) > len(second): 
            deduction = len(first) * remove_cost
            total_remove_cost += deduction
        elif(len(second) > len(first)) : 
            addition = len(second) * add_cost
            total_additional_cost += addition
        ans = total_remove_cost + total_additional_cost

        return ans
#     else :
#         return 0  #extra character 1 * 5
#removng 1 t 1 * 4 


#issues with first approach

# Incorrect Handling of Repeated Characters

# Your current logic only checks if a character is present in a sign, not how many times it appears.
# Example: old_sign = "aaa", new_sign = "a" should only remove two as, not all three.
# Using set() Instead of Comparing Character Frequencies

# set() ignores duplicates, so it fails when the signs have repeated letters with different counts.
# Complexity Issues with list(set(...))

# Creating sets and lists repeatedly increases runtime, especially for long strings.
from collections import Counter


def estimate_(add_cost, remove_cost, old_sign, new_sign):
    old_count = Counter(old_sign)
    new_count = Counter(new_sign)
    
    total_cost = 0
   

    for char,count in old_count.items():
        if count > new_count[char] : # If old sign has extra occurrences
            total_cost += (count - new_count[char]) * remove_cost
                
    for char,count in new_count.items():
        if count > old_count[char] : # If new sign needs more occurrences
            total_cost +=  (count - old_count[char]) * add_cost

       
    return total_cost
# print(estimate_(5, 7 , 'pmeznjzsfr', 'hnazmalyzdjbcj'))



#final answer using leveshtein algorithm
def estimate__(add_cost, remove_cost, old_sign, new_sign):
    m, n = len(old_sign), len(new_sign)  # Get lengths of both strings

    # Step 1: Create a DP table (2D list) initialized with 0
    dp = [[0] * (n + 1) for _ in range(m + 1)] 

    # Step 2: Fill the first row (transforming empty string to new_sign)
    for j in range(1, n + 1):
        dp[0][j] = j * add_cost  # Every added character costs add_cost

    # Step 3: Fill the first column (transforming old_sign to empty string)
    for i in range(1, m + 1):
        dp[i][0] = i * remove_cost  # Every removed character costs remove_cost

    # Step 4: Fill the DP table using nested loops
    for i in range(1, m + 1):  # Loop through old_sign
        for j in range(1, n + 1):  # Loop through new_sign
            if old_sign[i - 1] == new_sign[j - 1]:  
                # If the characters are the same, no cost
                dp[i][j] = dp[i - 1][j - 1]
            else:
                # Calculate possible costs
                insert = dp[i][j - 1] + add_cost  # Add character
                delete = dp[i - 1][j] + remove_cost  # Remove character
                replace = dp[i - 1][j - 1] + (add_cost + remove_cost)  # Replace character
                
                # Take the minimum cost operation
                dp[i][j] = min(insert, delete, replace)
    for row  in dp:
        print(row)

    # Step 5: The final answer is stored in dp[m][n]
    return dp[m][n]
# print(estimate__(5, 7 , 'abc', 'adc'))

#check out convo https://chatgpt.com/share/67bd72d9-f7e0-8010-ac5b-0c92624769d7
# lowercase_dict = {chr(i): i - 96 for i in range(97, 123)}
# uppercase_dict = {chr(i): i - 38 for i in range(65, 91)}
# print(uppercase_dict)