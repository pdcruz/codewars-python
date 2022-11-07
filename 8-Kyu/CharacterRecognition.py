# Character recognition software is widely used to digitise printed texts. Thus the texts can be edited, searched and stored on a computer.
# 
# When documents (especially pretty old ones written with a typewriter), are digitised character recognition softwares often make mistakes.
# 
# Your task is correct the errors in the digitised text. You only have to handle the following mistakes:
# 
#     S is misinterpreted as 5
#     O is misinterpreted as 0
#     I is misinterpreted as 1
# 
# The test cases contain numbers only by mistake.
def correct(text):
    corrections = {"5":"S", "0":"O", "1":"I"}
    new = text

    for i in corrections.keys():
        new = new.replace(i, corrections[i])

    return new


# Solution that uses string methods to translate
def correct_Solution(text):
    return text.translate(str.maketrans("501", "SOI"))


# Simple solution using replace
def correct_Solution2(text):
    return text.replace("5","S").replace("0","O").replace("1","I")


# Tests
print(correct_Solution2("J. R. R. T0LK1EN - THE L0RD 0F THE R1NG5"))
print(correct_Solution2("ERNE5T HEM1NGWAY - THE 0LD MAN AND THE 5EA"))