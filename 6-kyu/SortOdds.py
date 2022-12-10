# You will be given an array of numbers. 
# You have to sort the odd numbers in ascending order while leaving the even numbers at their original positions.
# 
# Examples
# 
# [7, 1]  =>  [1, 7]
# [5, 8, 6, 3, 4]  =>  [3, 8, 6, 5, 4]
# [9, 8, 7, 6, 5, 4, 3, 2, 1, 0]  =>  [1, 8, 3, 6, 5, 4, 7, 2, 9, 0]
def sort_array(arr):
    odds = sorted([n for n in arr if n % 2 == 1])
    result = [n if n % 2 == 0 else 'x' for n in arr]

    for n in odds:
        result[result.index('x')] = n
    
    return result


# Clever solution using list comprehension and reverse sorted odds list acting as a stack
def sort_array_solution(arr):
    odds = sorted([x for x in arr if x%2 != 0], reverse=True)
    return [x if x%2==0 else odds.pop() for x in arr]


test = [5, 3, 2, 8, 1, 4]

print(sort_array(test))