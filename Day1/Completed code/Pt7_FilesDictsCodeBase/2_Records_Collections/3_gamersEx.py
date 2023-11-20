
"To Do: Task 3:" 

"Complete the program below by replacing the question marks with the missing code"
playersList = ?  # create an empty list
addPlayer = True  # flag varible of boolean Type set to True

"The variables below have been created for you to ask for the respective user input"
# pName = playerName ,pPass =playerPass ,pScore = playerName,pHscore = playerHscore

# Use a while loop to keep asking for the details  playerName,pScore ,playerPass, playerHighScore

# Store the values in their respective variables above

# Exit the loop when you have at least two gamers

# While True execute the code below until the conditin is no longer True


while addPlayer:
# ask for user input respectively
    ?= ?
    ?= ?
    ?= ?
    ?= ?
#Exercise:  Create a dictionary below to hold player profiles
#Here you need to assign the values captured and stored in the variables to a key
# an example of a key has been done for you
    playerProfile = {
        "playerTag": pName,
        ?  : ?,
        ?  : ?,
        ?  : ?,
    }
    # add a player profile to playerList datatatype declared on line 1 using the append method
    playersList.?(?) 
    # Why would you use .upperMethod?
    anotherPlayer = input("Do you want to add another player? Y/N ").upper() 
    if anotherPlayer == "N":  # check/compare user response with the value "N"
        addPlayer = False  # reset the value asssign to addPlayer to "False"

"Exercise: print all the players you have added to the list"
print(f"List of players:\n {?} ")


# write data to file, using one of the previous write method examples ?
with open("add your path to file here/add filetowriteto.txt", "a") as file1Path:
    strData = str(?)  # convert list to string
    file1Path.write(f"\n{strData}")


"This is the output if you added four gamers. Take note of the index"
#      0                1                       2                         3......
# {'playerTag': 'p1', 'playerPass': 'pass1', 'playerScore': 1, 'playerHscore': 2}, 0
# {'playerTag': 'p2', 'playerPass': 'pass2', 'playerScore': 3, 'playerHscore':4},  1
# {'playerTag': 'p3', 'playerPass': 'pass3', 'playerScore': 5, 'playerHscore':6},  2
# {'playerTag': 'p4', 'playerPass': 'pass4', 'playerScore': 7, 'playerHscore':8}  3

aRecord = int(input("Enter the number(index position) of the record to be displayed "))
# access a specific player record base on the index value that matches the index position
aPlayer = playersList[aRecord]  # index = 1
print(f"The player details are: {aPlayer} ")
# {"playerTag": "BB", "playerPass": "bPass", "curScore": 56,   "highScore": 789},  #1
aPlayerAttribute = input(f"What attribute from {aPlayer} you want to print ")
# {"playerTag": "BB", "playerPass": "bPass", "curScore": 56,   "highScore": 789},  #1
print(f"The player {aPlayerAttribute} =  {aPlayer[aPlayerAttribute]}: ")


"""The aim of this exercise is to understand what the program is doing, especially saving
and accessing as many records as possible for each gamer"""




