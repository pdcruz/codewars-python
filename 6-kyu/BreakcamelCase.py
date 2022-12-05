# Complete the solution so that the function will break up camel casing, using a space between words.
# Example
# 
# "camelCasing"  =>  "camel Casing"
# "identifier"   =>  "identifier"
# ""             =>  ""
def break_camel_case(s):
    result = ''

    for l in s:
        if l.isupper():
            result += ' '
        result += l

    return result 


# OBVIOUSLY
# solution using list comprehension
def break_camel_case_solution(s):
    return ''.join(' ' + c if c.isupper() else c for c in s)



# tests
test = "breakCamelCase"
result = break_camel_case(test)

print(result)