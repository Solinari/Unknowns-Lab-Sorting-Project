# This project was to make an
# alternating/randomizing sorting function
# for a Microbiology Unknowns Lab

import random

# lists of element pairs: [bug, quantity remaining]
# bug is a string, quantity is an integer
# for this particular list, there are 40 of each
# the values can be changed to suit any size
# there should always be an equal number of gram Neg/Pos bugs
myBugsNeg = [["C. freundii", 6],
             ["E. coli", 6],
             ["E. aerogenes", 6],
             ["K. pneumonia", 6],
             ["P. vulgaris", 6],
             ["Ps. aeroginosa", 5],
             ["Salm. enteritidis", 5]]

myBugsPos = [["S. aureus", 9],
             ["S. epidermidis", 11],
             ["Strep. pyogenes", 10],
             ["Strep. faecalis", 10]]

# final list to print
myUnknowns = []

# this true-false pair is just to make each new list pseudorandom
# yet alternating from gram positive to negative or vice versa
# doing this was the goal of this project as in real life
# I would make several of these lists by hand for all sections
# of our Microbiology labs in the past.
isGramNeg = [True, False]

def printup():
    '''print out my now sorted list'''
    global myUnknowns

    # Using a formated print statement for this
    for i in range(0, len(myUnknowns), 4):
        print("{}) {} {}) {} {}) {} {}) {}\n".format(i + 1, myUnknowns[i],
                                                     i + 2, myUnknowns[i + 1],
                                                     i + 3, myUnknowns[i + 2],
                                                     i + 4, myUnknowns[i + 3]))

def Listpicker(isGramNeg):
    '''returns true or false for which list I want to pick from'''

    NegOrPos = random.choice(isGramNeg)

    return NegOrPos

def Unknowner(bugsNeg, bugsPos):
    '''puts together the intital list'''
    # randomly insert a bug from either the negative
    # or positive list of bugs using a random variable

    global myUnknowns

    mychoice = Listpicker(isGramNeg)
    
    while len(bugsNeg) > 0 or len(bugsPos) > 0:
    
        # if true append a choice from the gram negative list
        # then remove that choice
        if mychoice == True:

            # append a random choice
            thisbug = random.randint(0, len(bugsNeg) - 1)
            myUnknowns.append(bugsNeg[thisbug][0])

            # decrement that choice 
            bugsNeg[thisbug][1] -= 1

            # remove it if it now has 0 remaining
            if bugsNeg[thisbug][1] == 0:
                bugsNeg.remove(bugsNeg[thisbug])

            # switch mychoice to false and continue
            mychoice = False
            continue

        if mychoice == False:

            # append a random choice
            thisbug = random.randint(0, len(bugsPos) - 1)
            myUnknowns.append(bugsPos[thisbug][0])

            # decrement that choice 
            bugsPos[thisbug][1] -= 1

            # remove it if it now has 0 remaining
            if bugsPos[thisbug][1] == 0:
                bugsPos.remove(bugsPos[thisbug])

            # switch mychoice to false and continue
            mychoice = True

    printup()

# And now to run the function and generate our list!    
Unknowner(myBugsNeg, myBugsPos)


