# Given an array of integers as strings and numbers, return the sum of the array values as if all were numbers.
# Return your answer as a number.
def sum_mix(arr):
    
    result = 0

    for x in arr:
        if type(x) != type(1):
            result += int(x)
        else:
            result += x
    
    return result


# Solution 1 using map function
# map(func, iter) applies func to each element of iter, and returns list of results
def sum_mix_Solution1(arr):
    return sum(map(int, arr))

# Solution 2 using compact syntax
# Note that both of the solutions apply the conversion without checking,
# whereas my solution does actually check the type before attempting to convert.
# More efficient? dunno man but at least I'm thinking about it.
def sum_mix_Solution(arr):
    return sum(int(i) for i in arr)