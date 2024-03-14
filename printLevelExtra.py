# 1
# 11
# 21
# 1211
# 111221
# 312211
# ...

# Based on the level sent in parameter of your function,
# you should print the number of rows resulting of this level.
# The sample above is LEVEL 6
#
# EXTRA : Now we have the right result, we want to print the LEVEL at the beginning of each line
#   like this for the sample above :
#
# 1: 1
# 2: 11
# 3: 21
# 4: 1211
# 5: 111221
# 6: 312211
#
# CHALLENGE: YOU SHOULD NOT HAVE MORE THAN TWO CHANGES AGAINST YOUR PREVIOUS CODE
#

def printLevel(levelOfPrinting = 1):
    line = '1'
    print(f'1: {line}')
    levelOfPrinting -= 1 # REDUCE the number of level to PRINT because we already print one above

    # BEWARE the 'levelOfPrinting' has been reduced JUST BEFORE and it is not representing the entire number of lines !
    # INSTRUCTION: COPY YOUR PREVIOUS CODE HERE


printLevel(6)
printLevel(8)
printLevel(12)