# Complete the solution so that it returns true if the first argument(string) passed in ends with the 2nd argument (also a string).
# 
# Examples:
# 
# solution('abc', 'bc') # returns true
# solution('abc', 'd') # returns false
def ends_with(text, ending):
    return text[-1*len(ending):] == ending if len(ending)>0 else True


# Actual solution using handy string function
# see also: startswith()
def ends_with_solution(text, ending):
    return text.endswith(ending)