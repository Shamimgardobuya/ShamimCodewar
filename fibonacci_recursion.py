

#print all fibonacci numbers in the sequnce
#base case, when my_num is 0
# base case, when my_num is 1
#logic will be n-1 + n-2 
def fibonacci(my_num):  #O(1)
    if my_num == 0:
        return 0
    elif my_num == 1:
        return 1
    else:
        # print(my_num)

        return fibonacci(my_num - 1) + fibonacci(my_num - 2)   #O(2^n) for time and O(n) for space
    
# print(fibonacci(5)) #5
my_list = [  fibonacci(i) for i in range(60)]
print(my_list)
    