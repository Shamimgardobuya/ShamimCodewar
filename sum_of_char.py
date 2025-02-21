# instructions
# The main idea is to count all the occurring characters in a string.
# If you have a string like aba, then the result should be {'a': 2, 'b': 1}.

# What if the string is empty? Then the result should be empty object literal, {}.


# intial solution 
# why It Fails

# Let's say we process the string "XXY":
# X appears first → flag = 1
# X appears again → flag += 1 → flag = 2
# Y appears → flag = 1
# The next time X appears, 
# the flag should have been 3, but it’s reset incorrectly.
def count(s):
    # The function code should be here
    #string input
    #output is number of times of each character
    #create an empty dictionary
    #create a flag to keep counter
    #loop tthorugh the string
    #if key is in dictionary, increament flag else flag is just one
    ans = {}
    flag = 0
    if (len(s) > 0): 
        for i , char in enumerate(s):
            if (char  in ans) :
                
                flag+=1
                ans[char] = flag  #flag was shared amongst all characters hence this could occur
                
            else:
                flag = 1
                ans[char] = flag
        return ans
    else :
        return {}
    
# print(count('dXRwYFRutozXqkxbcJNmXqOZotKziRCFyxlCrpSigzO'))
#final solution
def count(s):
    # The function code should be here
    #string input
    #output is number of times of each character
    #create an empty dictionary
    #create a flag to keep counter
    #loop tthorugh the string
    #if key is in dictionary, increament flag else flag is just one
    ans = {}
    if (len(s) > 0): 
        for char in s:
            if (char  in ans) :    
                ans[char] += 1   
            else:      
                ans[char] = 1
        return ans
    else :
        return {}