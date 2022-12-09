# Build a pyramid-shaped tower, as an array/list of strings, given a positive integer number of floors. 
# A tower block is represented with "*" character.
# 
# For example, a tower with 3 floors looks like this:
# 
# [
#   "  *  ",
#   " *** ", 
#   "*****"
# ]
# 
# And a tower with 6 floors looks like this:
# 
# [
#   "     *     ", 
#   "    ***    ", 
#   "   *****   ", 
#   "  *******  ", 
#   " ********* ", 
#   "***********"
# ]

def build_tower(n):
    tower = []
    base = 2*n - 1

    for i in range(1,n+1):
        floor = 2*i - 1
        tower.append((floor * '*').center(base))

    return tower


# solution
# same logic as mine, but syntax compacted into one line
# NOTE the placement of for loop!
def build_tower_solution(n):
    return [('*' * (2*i-1)).center(2*n-1) for i in range(1, n+1)]


# tests
res = build_tower(6)
print(res)