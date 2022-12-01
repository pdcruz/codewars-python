# There is an array with some numbers. All numbers are equal except for one. Try to find it!
# 
# find_uniq([ 1, 1, 1, 2, 1, 1 ]) == 2
# find_uniq([ 0, 0, 0.55, 0, 0 ]) == 0.55
# 
# It’s guaranteed that array contains at least 3 numbers.
# 
# The tests contain some very huge arrays, so think about performance.

# Not sure why I took such a convoluted method here...
def find_unique(arr):
    low = min(arr)
    high = max(arr)
    counts = {arr.count(high):high, arr.count(low):low}

    return counts[1]


# Solution using set conversion
# Set will only contain DISTINCT members
def find_unique_solution(arr):
    a,b = set(arr)
    return a if arr.count(a) == 1 else b