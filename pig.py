# Move the first letter of each word to the end of it, then add
# "ay" to the end of the word. Leave punctuation marks untouched.

# solution
def pig_it(text):
    #your code here
    #split the string
    #using for loop, create a list with the first characters and add ay
    #create another list, this time it will have the removed items , merge the two list 
    
    
    new_text = text.split(" ")
    ay_list = []
    rem_list = []
    
    for i, char  in enumerate(new_text):
        new_char = new_text[i][0] + "ay" 
        ay_list.append(new_char)
        rem_list.append(new_text[i][1:])
    
    ans = []
    for i in zip(rem_list, ay_list):  #loopin g less length
        x = "".join(i)
        ans.append(x)
    return " ".join(ans)


#edge case what about the special characters, s
#done
import re
def pig_it(text):
    #your code here
    #split the string
    #using for loop, create a list with the first characters and add ay
    #create another list, this time it will have the removed items , merge the two list 
    
    special_xters = "".join(re.findall(r"[!?\=]", text))
    
    new_text = text.split(" ")
    ay_list = []
    rem_list = []
    
    for i, char in enumerate(new_text):
        if (new_text[i][0].isalpha()) :
            new_char = new_text[i][0] + "ay" 
            ay_list.append(new_char)
            rem_list.append(new_text[i][1:])
        else:
            ay_list.append(new_text[i])
            rem_list.append(new_text[i][1:])
            
    
    ans = []
    for i in zip(rem_list, ay_list):
        x = "".join(i)
        ans.append(x)
    final = " ".join(ans)
    return final


#refacotr time with list comprehension

import re
   
def pig_it(text):
    #your code here
    #split the string
    #using for loop, create a list with the first characters and add ay
    #create another list, this time it will have the removed items , merge the two list 
    
    #list comprehension is dope
    return " ".join(
        word[1:] + word[0] + "ay" if word.isalpha() else word
        for word in text.split()
    )
    
