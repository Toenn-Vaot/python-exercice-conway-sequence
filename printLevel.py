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

def printLevel(levelOfPrinting = 1):
    previousLine = '1'
    print(previousLine)
    levelOfPrinting -= 1 # REDUCE the number of level to PRINT because we already print one above

    # INSTRUCTION: WRITE YOUR CODE HERE

printLevel(6)
printLevel(8)
printLevel(24)