from collections.abc import Iterable


# Complete the function/method (depending on the language)
# to return true/True when its argument is an array that 
# has the same nesting structures and same corresponding
# length of nested arrays as the first array.

# For example:

# # should return True
# same_structure_as([ 1, 1, 1 ], [ 2, 2, 2 ] )
# same_structure_as([ 1, [ 1, 1 ] ], [ 2, [ 2, 2 ] ] )

# fruits = ["apple", "banana", "cherry"]
# colors = ["red", "yellow", "dark red"]

# for fruit, color in zip(fruits, colors):
#     print(f"The {fruit} is {color}.")

def same_structure_as(original,other):    
    if (type(original) == list and type(other) == list and len(original) == len(other)) :
        for org , other in zip(original, other) :
            if(type(org) == list and type(other) == list and len(org) == len(other)): 
                # print('fels')
                return True
            elif(type(org) == list and type(other) == list and len(org) != len(other)):
#                 print("here")
                return False
            # elif(isinstance(org, Iterable) and not isinstance(other, Iterable) or isinstance(other, Iterable) and not isinstance(org, Iterable)):
            #     return False
        return True
    else:
        return False
    
    
# print(same_structure_as([[[],[]]] , [[2,2],2] )) # false
# [1,[1,1]] not same as [[2,2],2]: True should equal False



#reviewed code - above code only did a high level checkof the array and did  not consider other elements of the array
#below utilizes recursion to do checks in all elements of array 
def same_structure_as(original, other):
    if isinstance(original, list) and isinstance(other, list):
        if len(original) != len(other):
            return False
        return all(same_structure_as(o1, o2) for o1, o2 in zip(original, other))  #returns true if all elements in iterable are true
    else:
        return not isinstance(original, list) and not isinstance(other, list)


#custom way without all
def same_structure_as(original, other):
    if isinstance(original, list) and isinstance(other, list):
        if len(original) != len(other):
            return False
        
        for o1, o2 in zip(original, other):
            if not same_structure_as(o1, o2):
                return False
        return True
    else:
        return not isinstance(original, list) and not isinstance(other, list)



# Write a function that takes a nested list 
# and returns a flat list containing all the elements, 
# no matter how deep they are.
# flatten([1, [2, 3], [[4], 5]])       # → [1, 2, 3, 4, 5]
# flatten([[[[1]]], 2])               # → [1, 2]
# flatten([1, [2, [3, [4, [5]]]]])    # → [1, 2, 3, 4, 5]

#i have only one list
#return a new list with all the elements without nesting any
#continue getting into the nested array until you find an integer 
def flatten_list(nested_list):
    flat_list = []
    if (len(nested_list) == 0) :
        return []
    for i in nested_list :
        if isinstance(i, int):
            flat_list.append(i)
        else:
            flat_list.extend(flatten_list(i))
    return flat_list
# print(flatten_list([1, [2, 3], [[4], 5]] ))       # → [1, 2, 3, 4, 5]      
            
            
# Write a function that returns the
# maximum depth of a nested list.

# max_depth([1, 2, 3])                   # → 1
# max_depth([1, [2, 3]])                # → 2
# max_depth([1, [2, [3, [4]]]])         # → 4
# max_depth([[[]]])                     # → 3
# max_depth([])                         # → 1

#create a value having a value of 0 for starting
#when it gets an item that is an int, add i value
#if it gets a list , increament value as 1 until no more lists 




# “Of all the depths from each i, 
# what’s the highest? Then add 1 for this level.”


def max_depth(nested_list):  
    if not nested_list:
        return 1
    max_sub_depth  = 0
    for i in nested_list :
        if isinstance(i, list):
            sub_depth = max_depth(i)
            if( sub_depth > max_sub_depth):
                max_sub_depth = sub_depth
    return max_sub_depth + 1

# print(max_depth([1, [2, [3, [4, 5]]], 6] ))       # → [1, 2, 3, 4, 5] 
            


# Write a recursive function that takes a nested list 
# and counts how many list objects are inside 
# (including nested ones, but excluding the outermost one).

# Traverses the list

# For every element that’s a list, 
# increments a counter

# Then recursively calls itself on that 
# sublist to count further



def count_lists(nested_list):
    if not isinstance(nested_list, list):
        return 0
    
    count = 1
    for i in nested_list:
        if isinstance(i, list): 
            # count = 1
            # print('count_value_b4 recursion ', count, 'i', i)

            count += count_lists(i)
            # print('count_value_after recursion ', count, 'i', i)
    return count     # Exclude the outermost list

# def remove_one(count):
#     if count > 0:
#         return count - 1
#     return 0

# print(count_lists([1, 2, 3]))                     # → 0
# print(count_lists([1, [2, 3]]))                  # → 1
# print(count_lists([1, [2, [3, [4]]]]))           # → 3
# print(count_lists([[[]]]))                       # → 1
# print(count_lists([]))                           # → 0
print(count_lists([1, [2, 3], [[4], 5]]))        # → 2



