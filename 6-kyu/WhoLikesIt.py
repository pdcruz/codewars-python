# You probably know the "like" system from Facebook and other pages. People can "like" blog posts, pictures or other items. 
# We want to create the text that should be displayed next to such an item.
# 
# Implement the function which takes an array containing the names of people that like an item. 
# It must return the display text as shown in the examples:
# 
# []                                -->  "no one likes this"
# ["Peter"]                         -->  "Peter likes this"
# ["Jacob", "Alex"]                 -->  "Jacob and Alex like this"
# ["Max", "John", "Mark"]           -->  "Max, John and Mark like this"
# ["Alex", "Jacob", "Mark", "Max"]  -->  "Alex, Jacob and 2 others like this"
# 
# Note: For 4 or more names, the number in "and 2 others" simply increases.
def likes(names):

    total = len(names)
    
    match total:
        case 0:
            result = "no one likes this"
        case 1:
            result = "{0} likes this".format(names[0])
        case 2:
            result = "{0} and {1} like this".format(names[0], names [1])
        case 3:
            result = "{0}, {1} and {2} like this".format(names[0], names [1], names[2])
        case _:
            result = "{0}, {1} and {2} others like this".format(names[0], names [1], total - 2)
    
    return result


# Solution using dictionary. Conmments from author ChiaraBells
#
# make a dictionary d of all the possible answers. 
# Keys are the respective number of people who liked it.
# 
# {} indicate placeholders. They do not need any numbers but are simply replaced in the order the arguments in names are given to format()
# {others} can be replaced by its name; below the argument "others = total - 2" is passed to str.format()
def likes_solution(names):

    d = {
        0: "no one likes this",
        1: "{} likes this",
        2: "{} and {} like this",
        3: "{}, {} and {} like this",
        4: "{}, {} and {others} others like this"
    }

    total = len(names)

    # d[min(4, total)] insures that the appropriate string is called from the dictionary
    # and subsequently returned. Min is necessary as len(names) may be > 4
    
    # The * in *names ensures that the list names is blown up and that format is called
    # as if each item in names was passed to format individually, i. e.
    # format(names[0], names[1], .... , names[n], others = total - 2
    return d[min(4, total)].format(*names, others = total - 2)