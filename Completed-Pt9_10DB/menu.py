import readsongs, addsongs, updatesongs, deletesongs, reports

# create function 
def menuFile():
    with open('Week10/Pt9_10DB/songsMenu.txt') as songMenuFile:

        # read from the menu file and assign it to a variable
        songFileData = songMenuFile.read()

        return songFileData
    
# print(menuFile())

def songsMenu():
    option = 0 # initialise the option variable with an integer value 0
    optionsList = ["1","2","3","4","5","6"]

    # initialise the menu file function with the choiceMenu variable 
    choiceMenu = menuFile() 

    while option not in optionsList:
        # call/invoke the function though the variable choiceMenu
        print(choiceMenu) # display the options from the menu file

        # re-assign the value of the option variable 
        option = input("Enter an option from the songs Main menu: ")
        # if user input is not on the list
        if option not in optionsList:
            # do this/execute the code below
            print(f"{option} is not a valid choice! ")
    return option
# print(songsMenu())

# create a boolean variable 
mainProgram = True

while mainProgram: # while True
    # initialise the songsMenu function with the choiceMenu mainSongsMenu 
    mainMenu = songsMenu()

     # if the user input is string value 1
    if mainMenu == "1":
       # , then call the function the readsongs file
        readsongs.read_songs()

    elif mainMenu == "2":
        addsongs.insert_songs()

    elif mainMenu == "3":
        updatesongs.update_songs()

    elif mainMenu == "4":
        deletesongs.delete_songs()
    
    elif mainMenu == "5":
        reports.reports()
    
    else:
        # reassign the boolean variable of 'mainProgram' False
        mainProgram = False
input("Enter to quit songs App")


  





