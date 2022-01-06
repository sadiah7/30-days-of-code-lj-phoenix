# Raam is superstitious. He will only use a number as a roll number
# if all digits of the number are different(i.e. no digits are repeated)
# Return boolean string as output, print true if all digits are different and false if there are repetitions.
def lucky():
    num = str(input())
    dc = {}
    for i in num:
        if i not in dc:
            dc[i] = 0
        dc[i] += 1
    for value in dc.values():
        if value > 1:
            return "The number is unlucky."
    return "The number is lucky."


print(lucky())
