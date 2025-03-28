# Given a non-negative integer 

# x, find the integer part of its square root
# using binary search.

# Example Inputs & Outputs:
# ✅ sqrt_binary_search(16) → 4
# ✅ sqrt_binary_search(27) → 5
# ✅ sqrt_binary_search(50) → 7
# ✅ sqrt_binary_search(1) → 1
# ✅ sqrt_binary_search(0) → 0

#need to have a low and  
# a high bound
#square the mid and
# if mid squared is close to the x value 
#return integer,
#handle edge cases corectly

def find_square_root(x):
    ans = 0
    low, high = 1, x
    if(x == 1 or x == 0 ) :
        return x
    if (x == 0) :
        return 0
    while (low <= high) :
        mid = low + (high - low) // 2
        value = mid * mid
        if( value == x):
            return mid
        elif(value < x):
            ans = mid
                
            low = mid + 1
        else:
        
            high = mid - 1
    return ans
    
# print(find_square_root(0))



# Given a sorted array of integers and
# a target value, find the first and 
# last index where the target appears. 
# If the target is not found, return [-1, -1].

# 🔹 Example Inputs & Outputs:
# ✅ find_first_last([5, 7, 7, 8, 8, 10], 8) → [3, 4]
# ✅ find_first_last([5, 7, 7, 8, 8, 10], 6) → [-1, -1]
# ✅ find_first_last([1, 2, 2, 2, 3, 4], 2) → [1, 3]
# ✅ find_first_last([1, 2, 3, 4, 5], 3) → [2, 2]
# ✅ find_first_last([], 3) → [-1, -1]


# 
def find_target_first_and_last_occurrence(list_, target):
    low, high = 0, len(list_) - 1 
    count_target = 0
    last_occurrence = -1
    while (low <= high) :
        mid = low + (high - low ) // 2
        if (list_[mid] == target) :
            count_target = list_.count(target)  #O(n)
            if count_target > 1 :
                last_occurrence = mid + (count_target - 1)
                return [mid , last_occurrence]

            else:
                return [mid, mid]
            
        elif(list_[mid] < target):
            low = mid + 1
        else:
            high = mid - 1
    return [-1, -1]

print(find_target_first_and_last_occurrence([5, 7, 7, 8, 10], 8))
        
# def last_occurrence():
        
#better complexisty solution 
def find_target_first_and_last_occurrence(arr, target):
    def find_boundary(find_first):
        low, high = 0, len(arr) - 1
        boundary = -1
        while low <= high:
            mid = (low + high) // 2
            if arr[mid] == target:
                boundary = mid  # Potential first/last occurrence
                if find_first:
                    high = mid - 1  # Move left for first occurrence
                else:
                    low = mid + 1  # Move right for last occurrence
            elif arr[mid] < target:
                low = mid + 1
            else:
                high = mid - 1
        return boundary

    first = find_boundary(True)
    last = find_boundary(False)
    return [first, last]

# Test cases
print(find_target_first_and_last_occurrence([5, 7, 7, 8, 8, 10], 8))  # [3, 4]
print(find_target_first_and_last_occurrence([5, 7, 7, 8, 8, 10], 6))  # [-1, -1]
print(find_target_first_and_last_occurrence([1, 2, 2, 2, 3, 4], 2))  # [1, 3]
print(find_target_first_and_last_occurrence([1, 2, 3, 4, 5], 3))  # [2, 2]
print(find_target_first_and_last_occurrence([], 3))  # [-1, -1]
