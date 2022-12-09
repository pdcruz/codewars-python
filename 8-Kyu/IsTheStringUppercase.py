# Create a method to see whether the string is ALL CAPS.
# 
# In this Kata, a string is said to be in ALL CAPS whenever it does not contain any lowercase letter 
# so any string containing no letters at all is trivially considered to be in ALL CAPS.
# 
# Examples (input -> output)
# 
# "c" -> False
# "C" -> True
# "hello I AM DONALD" -> False
# "HELLO I AM DONALD" -> True
# "ACSKLDFJSgSKLDFJSKLDFJ" -> False
# "ACSKLDFJSGSKLDFJSKLDFJ" -> True
# "$%&" -> True
def is_uppercase(inp):
    return sum([1 for c in inp.replace(' ','') if c.islower()]) == 0


# AGAIN obvious solution
# get some sleep
def is_uppercase_solution(inp):
    return inp.upper() == inp


test = '5438257'
print(is_uppercase(test))