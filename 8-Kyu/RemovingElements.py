# Take an array and remove every second element from the array. Always keep the first element and start removing with the next element.
# 
# Example:
# ["Keep", "Remove", "Keep", "Remove", "Keep", ...] --> ["Keep", "Keep", "Keep", ...]
# 
# None of the arrays will be empty, so you don't have to worry about that!

def remove_every_other(my_list):

    result = []

    for i in range(0,len(my_list),2):
        result.append(my_list[i])

    return result


# Solution using indexing:
# list[i:j:k] takes a the slice of list starting at element i, to element (j-1), with step size k 
def remove_every_other_Solution(my_list):
    return my_list[::2]