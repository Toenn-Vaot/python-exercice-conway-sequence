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

    # FOR EACH level IN levelOfPrinting, do ...
    # NOTICE: 
    #   We introduce a variable 'i' this time because we will use it to PRINT the 'line' number
    for i in range(levelOfPrinting):
        currentChar="" # PREPARE the 'currentChar' to host the latest read character (emptied at the beginning of reading)
        countCurrentChar=0 # PREPARE the 'countCurrentChar' to host the count of 'currentChar' READ until finding a different one (reset to zero at the beginning of reading)
        currentLine="" # PREPARE the 'line' to print AFTER reading the 'line' (emptied at the beginning of reading)

        # FOR EACH character IN the STRING currentLine (~ ARRAY of char)
        for char in line:
            # IF the 'currentChar' is EMPTY...
            if(currentChar == ""):          
                # LOGIC: ... we set it to the read 'char'
                currentChar = char
            
            # IF the 'currentChar' (saved one) IS NOT EQUAL to read 'char'
            if(currentChar != char):
                # SAVE the template {countCurrentChar}{currentChar} concatenate to {currentLine}
                # NOTICE: AT LEVEL 2 & 3, we never pass in this code BECAUSE the 'currentChar' keep the same until the END
                # NOTICE: AT LEVEL 4, we will pass one time to obtain respectively
                #           currentLine = "{}{1}{2}"
                # NOTICE: AT LEVEL 5, we will pass two times to obtain respectively
                #           currentLine = "{}{1}{1}"
                #           currentLine = "{}{1}{2}"
                currentLine = f"{currentLine}{countCurrentChar}{currentChar}"
                currentChar = char # SET new character to current
                countCurrentChar = 0 # RESET counter of current

            # INCREMENT the counter in ALL CASES
            countCurrentChar += 1
        
        # NOTICE: Why concatenate here ?
        #   1st CASE : if the 'currentChar' never changed we will concatenate
        #   2nd CASE : when there are different characters in 'line', the last one is like the 1st CASE
        #               it will never be compared to a different character because it is the last one
        currentLine = f"{currentLine}{countCurrentChar}{currentChar}"

        # PRINT the 'currentLine'
        print(f'{i+2}: {currentLine}')
        # SET the 'line' to the 'currentLine' to continue the LOOP of LEVELS with the new printed line
        line=currentLine


printLevel(6)
printLevel(8)
printLevel(12)