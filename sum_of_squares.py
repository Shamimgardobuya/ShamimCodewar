

# Let's pretend your company just hired your friend from college and paid you a referral bonus. Awesome! To celebrate, you're taking your team out to the terrible dive bar next door and using the referral bonus to buy, and build, the largest three-dimensional beer can pyramid you can. And then probably drink those beers, because let's pretend it's Friday too.

# A beer can pyramid will square the number of cans in each level - 1 can in the top level, 4 in the second, 9 in the next, 16, 25...

# Complete the beeramid function to return the number of complete levels of a beer can pyramid you can make, given the parameters of:

# your referral bonus, and

# the price of a beer can

# For example:

# beeramid(1500, 2); // should === 12
# beeramid(5000, 3); // should === 16

# Pseudocode
# Beer can pyramid, squares the number of cans in each level 
# find number of cans bonus// price of 1
#  Find the complete levels by squaring normal squares and adding it up till it reaches the complete number of cans
# [n(n+1)(2n+1)] / 6
# 100*101*201 /6



def binarySearch(low, high, x):
    diff = []
    if (x < 1) :
        return 0
    while low <= high:

        mid = low + (high - low) // 2
        
        value =  (mid*(mid+1)*(2*mid+1)) / 6  #used sum of squares of n formula [n(n+1)(2n +1 )]/6
        if value == x :  
            return mid

        elif value < x :  
            diff.append((mid, value)) #using the numbers close to the value of x and storing them as tuples
            low = mid + 1       

        else:
            high = mid - 1

    highest = max(diff, key=lambda x: x[1]) #get max of the list values using the second element of the tuple
    highest_key = highest[0]
    if(highest_key) :
        return highest_key

    return -1
print(binarySearch(1, 100,  4))

#optimzation of the above 
def beeramid(bonus, price):
    diff = []
    x = bonus / price
    low  = 1
    high = 100
    if x < 1:
        return 0

    closest_n = -1  # To store the best possible n
    closest_value = float('-inf')  # Track closest sum value

    while low <= high:
        mid = low + (high - low) // 2
        value = (mid * (mid + 1) * (2 * mid + 1)) / 6  # Sum of squares formula

        if value == x:
            return mid  # Exact match found

        elif value < x:
            if value > closest_value:  # Update the closest approximation
                closest_n = mid
                closest_value = value
            low = mid + 1

        else:
            high = mid - 1

    return closest_n  # Return the closest integer n




#newtons method to estimate a high
# Start with a rough estimate – usually a cube root or square root approximation.

# Use Newton's formula:
# n_new =n−f 
# ′
#  (n)
# f(n)
# ​


# Iterate until it stabilizes – stop when the change is very small.

# Round up if needed – since n must be a whole number in our case.

def estimate_high(x):
    if x < 1:
        return 0

    n = (6 * x) ** (1/3)  # Initial rough estimate using cube root
    epsilon = 1e-6  # Convergence threshold (to stop when change is very small)

    iteration = 0  # To track the number of steps
    while True:
        f_n = (n * (n + 1) * (2 * n + 1)) / 6 - x
        f_prime_n = ((n + 1) * (2 * n + 1) + n * (2 * n + 1) + 2 * n * (n + 1)) / 6
        
        if f_prime_n == 0:
            break  # Avoid division by zero
        
        new_n = n - f_n / f_prime_n  # Newton's update formula

        print(f"Iteration {iteration}: n = {n:.6f}, f(n) = {f_n:.6f}, f'(n) = {f_prime_n:.6f}, new_n = {new_n:.6f}")

        if abs(new_n - n) < epsilon:  # Stop when the difference is very small
            break
        
        n = new_n
        iteration += 1  # Count iterations

    return int(n) + 1  # Convert to integer (rounding up)
print(estimate_high(5000/3))