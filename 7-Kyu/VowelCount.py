# Return the number (count) of vowels in the given string.
# 
# We will consider a, e, i, o, u as vowels for this Kata (but not y).
# 
# The input string will only consist of lower case letters and/or spaces.

# LOTS of different solutions for this one
# Here's mine, using our old mate the lambda function
# ACTUALLY understand the concept of anonymous function now
# Much better than my c# days
def vowel_count(sentence):
    vowels = {'a', 'e', 'i', 'o', 'u'}
    return sum(map(lambda x: x in vowels, sentence.lower()))


# Solution using list comprehension
def vowel_count_solution(sentence):
    return sum(1 for x in sentence.lower() if x in 'aeiou')


# Solution using membership test and boolean conversion
# Cleaner version of my solution
def vowel_count_solution2(sentence):
    return sum(c in 'aeiou' for c in sentence.lower())


# Another list comprehension approach
def vowel_count_solution3(sentence):
    return len([x for x in sentence.lower() if x in 'aeiou'])