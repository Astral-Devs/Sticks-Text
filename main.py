import random
import enemy

leftHandMc = 0
rightHandMc = 2
leftHandEn = 1
rightHandEn = 1

projectedMcleftHand = leftHandMc
projectedMcRightHand = rightHandMc
projectedEnLeftHand = leftHandEn
projectedEnRightHand = rightHandEn

leftHandMcAlive = True
rightHandMcAlive = True
leftHandEnAlive = True
rightHandEnAlive = True


numberOfFingers = 0

running = True

pickedIllegalAmount = True

def checkDeadHands():
    global running
    global leftHandMcAlive
    global rightHandMcAlive
    global leftHandEnAlive
    global rightHandEnAlive

    # check for dead hand for mc
    if leftHandMc == 0:
        leftHandMcAlive = False
    else:
        leftHandMcAlive = True

    if rightHandMc == 0:
        rightHandMcAlive = False
    else:
        rightHandMcAlive = True

    if leftHandMcAlive or rightHandMcAlive :
        pass
    else:
        print("you lost better luck next time")
        running = False

    if leftHandEn == 0:
        leftHandEnAlive = False
    else:
        leftHandEnAlive = True

    if rightHandEn == 0 :
        rightHandEnAlive = False
    else:
        rightHandEnAlive = True

    if leftHandEnAlive == False and rightHandEnAlive == False:
        print("you won and that is pog")
        running = False

def printAll():
    print("Left hand(MC): "+ str(leftHandMc))
    print("Right hand(MC): " + str(rightHandMc))
    print("Left hand(EN): " + str(leftHandEn))
    print("Right hand(EN): " + str(rightHandEn))

def attack():
    global leftHandEn
    global rightHandEn
    global leftHandMc
    global rightHandMc


    # allows you to chose which hand you want to attack with
    if leftHandMcAlive and rightHandMcAlive:
        askForHand = input("Which hand do you want to use\n"
                           "[1] Left\n"
                           "[2] Right\n")
        #Left hand
        if askForHand == "1":
            if leftHandEnAlive and rightHandEnAlive:
                askForEnemyHand = input("Which one of the ememy hand do you want to attack\n"
                                        "[1] Left\n"
                                        "[2] Right\n")
                if askForEnemyHand == "1":
                    leftHandEn += leftHandMc
                else:
                    rightHandEn += leftHandMc
            elif leftHandEnAlive:
                leftHandEn += leftHandMc
            else:
                rightHandEn += leftHandMc
        # Right hand
        else:
            if leftHandEnAlive and rightHandEnAlive:
                askForEnemyHand = input("Which one of the ememy hand do you want to attack\n"
                                        "[1] Left\n"
                                        "[2] Right\n")
                if askForEnemyHand == "1":
                    leftHandEn += rightHandMc
                else:
                    rightHandEn += rightHandMc
            elif leftHandEnAlive:
                leftHandEn += rightHandMc
            else:
                rightHandEn += rightHandMc
    # If only the left hand is alive
    elif leftHandMcAlive:
        if leftHandEnAlive and rightHandEnAlive:
            askForEnemyHand = input("Which one of the ememy hand do you want to attack\n"
                                    "[1] Left\n"
                                    "[2] Right\n")
            if askForEnemyHand == "1":
                leftHandEn += leftHandMc
            else:
                rightHandEn += leftHandMc
        elif leftHandEnAlive:
            leftHandEn += leftHandMc
        else:
            rightHandEn += leftHandMc
    #if only the right hand is alive
    elif rightHandMcAlive:
        if leftHandEnAlive and rightHandEnAlive:
            askForEnemyHand = input("Which one of the ememy hand do you want to attack\n"
                                    "[1] Left\n"
                                    "[2] Right\n")
            if askForEnemyHand == "1":
                leftHandEn += rightHandMc
            else:
                rightHandEn += rightHandMc
        elif leftHandEnAlive:
            leftHandEn += rightHandMc
        else:
            rightHandEn += rightHandMc
    printAll()



def enemyAttack():
    global leftHandMc
    global rightHandMc
    enemyHandUsed = random.randint(1,2)
    handAttacked = random.randint(1,2)
    if enemyHandUsed == 1:
        if handAttacked == 1:
            leftHandMc += leftHandEn
        else:
            rightHandMc += leftHandEn
    else:
        if handAttacked == 1:
            leftHandMc += rightHandEn
        else:
            rightHandMc += rightHandEn
    print("The enemy attacks!")
    printAll()


def resetMcProjection():
    global projectedMcRightHand
    global projectedMcleftHand

    projectedMcleftHand = leftHandMc
    projectedMcRightHand = rightHandMc


def projectRightMc():
    global rightHandMc
    global projectedMcRightHand
    global numberOfFingers

    resetMcProjection()

    projectedMcRightHand = rightHandMc - numberOfFingers
    print (rightHandMc)
    print(projectedMcRightHand)
    legalMove = False
    if rightHandMc > 1 & projectedMcRightHand < 1:
        legalMove = True
    else:
        legalMove = False

    return False

def projectLeftMc():
    global leftHandMc
    global projectedMcleftHand
    global numberOfFingers

    resetMcProjection()
    projectedMcleftHand = leftHandMc - numberOfFingers
    legalMove = False
    if leftHandMc > 1 & projectedMcleftHand < 1:
        legalMove = False
    else:
        legalMove = True

    return legalMove

def split():

    global leftHandEn
    global rightHandEn
    global leftHandMc
    global rightHandMc
    global numberOfFingers
    global pickedIllegalAmount


    while pickedIllegalAmount:
        if leftHandMcAlive and rightHandMcAlive:
            askForHand = input("Which hand do you want to add to?\n"
                               "[1] Left\n"
                               "[2] Right\n")
            if askForHand == "1":
                askForAmount = input("how many fingers do you want to transfer to that finger: ")
                numberOfFingers = int(askForAmount)

                if rightHandMc >= numberOfFingers & projectRightMc():
                    leftHandMc += numberOfFingers
                    rightHandMc -= numberOfFingers
                    pickedIllegalAmount = False

            else:
                askForAmount = input("how many fingers do you want to transfer to that finger: ")
                numberOfFingers = int(askForAmount)

                if leftHandMc >= numberOfFingers & projectLeftMc():
                    leftHandMc -= numberOfFingers
                    rightHandMc += numberOfFingers
                    pickedIllegalAmount = False

        elif leftHandMcAlive and leftHandMc > 1:
            askForAmount = input("how many fingers do you want to move over to your right hand: ")
            numberOfFingers = int(askForAmount)

            if leftHandMc >= numberOfFingers & projectLeftMc():
                leftHandMc -= numberOfFingers
                rightHandMc += numberOfFingers
                pickedIllegalAmount = False

        elif rightHandMcAlive and rightHandMc > 1:
            askForAmount = input("how many fingers do you want to move over to your left hand: ")
            numberOfFingers = int(askForAmount)

            if rightHandMc >= numberOfFingers & projectRightMc():
                leftHandMc += numberOfFingers
                rightHandMc -= numberOfFingers
                pickedIllegalAmount = False

        else:
            print("Hey thats illegal")
            pickedIllegalAmount = False

    printAll()


printAll()
while running:
    checkDeadHands()

    if running:
        askForMove = input("what do you want to do?\n"
                           "[1] Attack\n"
                           "[2] Split\n")
        if askForMove == "1":
            attack()
        else:
            pickedIllegalAmount = True
            split()

        enemyMove = random.randint(1,1)

        if enemyMove == 1:
            enemyAttack()
        else:
            print("yea")


