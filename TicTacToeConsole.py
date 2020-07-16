

mapListRow1= [" ","|"," ","|"," "]
mapListRow2= ["-","+","-","+","-"]
mapListRow3= [" ","|"," ","|"," "]
mapListRow4= ["-","+","-","+","-"]
mapListRow5= [" ","|"," ","|"," "]

positionList = ["topLeft","topCenter","topRight","middleLeft","middleCenter","middleRight","bottomLeft","bottomCenter","bottomRight"]

def drawGameBoard():
    print(mapListRow1[0]+mapListRow1[1]+mapListRow1[2]+mapListRow1[3]+mapListRow1[4])
    print(mapListRow2[0]+mapListRow2[1]+mapListRow2[2]+mapListRow2[3]+mapListRow2[4])
    print(mapListRow3[0]+mapListRow3[1]+mapListRow3[2]+mapListRow3[3]+mapListRow3[4])
    print(mapListRow4[0]+mapListRow4[1]+mapListRow4[2]+mapListRow4[3]+mapListRow4[4])
    print(mapListRow5[0]+mapListRow5[1]+mapListRow5[2]+mapListRow5[3]+mapListRow5[4])

def placePiece(playerOneTurn):
    if playerOneTurn == True:
        playerName = "Player One"
        playerPiece = "X"
    elif playerOneTurn == False:
        playerName = "Player Two"
        playerPiece = "O"

    print("Available spots are:")
    print(positionList)
    print("{}, where will you place your {}?".format(playerName, playerPiece))
    placePieceHere = input()
    if placePieceHere not in positionList:
        print("Sorry spot not available or typo")
    else:
        if placePieceHere == "topLeft":
            mapListRow1[0] = playerPiece
        elif placePieceHere == "topCenter":
            mapListRow1[2] = playerPiece
        elif placePieceHere == "topRight":
            mapListRow1[4] = playerPiece
        elif placePieceHere == "middleLeft":
            mapListRow3[0] = playerPiece
        elif placePieceHere == "middleCenter":
            mapListRow3[2] = playerPiece
        elif placePieceHere == "middleRight":
            mapListRow3[4] = playerPiece
        elif placePieceHere == "bottomLeft":
            mapListRow5[0] = playerPiece
        elif placePieceHere == "bottomCenter":
            mapListRow5[2] = playerPiece
        elif placePieceHere == "bottomRight":
            mapListRow5[4] = playerPiece
        drawGameBoard()
        positionList.remove(placePieceHere)

def xWinCheck():
    if mapListRow1[0] == "X" and mapListRow1[2] == "X" and mapListRow1[4] == "X":
        return True
    elif mapListRow3[0] == "X" and mapListRow3[2] == "X" and mapListRow3[4] == "X":
        return True
    elif mapListRow5[0] == "X" and mapListRow5[2] == "X" and mapListRow5[4] == "X":
        return True

    elif mapListRow1[0] == "X" and mapListRow3[0] == "X" and mapListRow5[0] == "X":
        return True
    elif mapListRow1[2] == "X" and mapListRow3[2] == "X" and mapListRow5[2] == "X":
        return True
    elif mapListRow1[4] == "X" and mapListRow3[4] == "X" and mapListRow5[4] == "X":
        return True

    elif mapListRow1[0] == "X" and mapListRow3[2] == "X" and mapListRow5[4] == "X":
        return True
    elif mapListRow5[0] == "X" and mapListRow3[2] == "X" and mapListRow1[4] == "X":
        return True


def oWinCheck():
    if mapListRow1[0] == "O" and mapListRow1[2] == "O" and mapListRow1[4] == "O":
        return True
    elif mapListRow3[0] == "O" and mapListRow3[2] == "O" and mapListRow3[4] == "O":
        return True
    elif mapListRow5[0] == "O" and mapListRow5[2] == "O" and mapListRow5[4] == "O":
        return True

    elif mapListRow1[0] == "O" and mapListRow3[0] == "O" and mapListRow5[0] == "O":
        return True
    elif mapListRow1[2] == "O" and mapListRow3[2] == "O" and mapListRow5[2] == "O":
        return True
    elif mapListRow1[4] == "O" and mapListRow3[4] == "O" and mapListRow5[4] == "O":
        return True

    elif mapListRow1[0] == "O" and mapListRow3[2] == "O" and mapListRow5[4] == "O":
        return True
    elif mapListRow5[0] == "O" and mapListRow3[2] == "O" and mapListRow1[4] == "O":
        return True


def gameLoop():
    while (len(positionList) is not 0):
        xWinCheck()
        if xWinCheck():
            print("Player One Wins")
            break
        elif oWinCheck():
            print("Player Two Wins")
            break

        else:
            placePiece(len(positionList)% 2 == 1)

    if(len(positionList) is 0):
        if xWinCheck():
            print("Player One Wins")
        elif oWinCheck():
            print("Player Two Wins")
        else:
            print("It's a Draw")



drawGameBoard()
gameLoop()
print("GameOver")
