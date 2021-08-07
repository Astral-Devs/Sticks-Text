import random
leftHandMc = 1
rightHandMc = 1



leftHandMcAlive = True
rightHandMcAlive = True

running = True

illegalMove = False

def checkDeadHands():
    global leftHandMcAlive
    global rightHandMcAlive
    if leftHandMc == 0:
        leftHandMcAlive = False

    if rightHandMc == 0:
        rightHandMcAlive = False

