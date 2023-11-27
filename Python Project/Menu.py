
import readfilms, addfilms, updatefilms, deletefilms, reports

#create function
def menuFile():
    with open('Python Project/filmsMenu.txt') as filmMenuFile:

        #read from menu and assign it to a varaible
        filmFileData = filmMenuFile.read()
        return filmFileData 
    

    """
#print(menuFile())

def filmsMenu():
    option = 0 # initialise the option variable with an integer value 0
    optionsList = ["1","2","3","4","5","6"]

    # initialise the menu file function with the choiceMenu variable 
    choiceMenu = menuFile() 

    while option not in optionsList:
        # call/invoke the function though the variable choiceMenu
        print(choiceMenu) # display the options from the menu file

        # re-assign the value of the option variable 
        option = input("Enter an option from the films Main menu: ")
        # if user input is not on the list
        if option not in optionsList:
            # do this/execute the code below
            print(f"{option} is not a valid choice! ")
    return option
# print(songsMenu())

# create a boolean variable 
mainProgram = True

while mainProgram: # while True
    # initialise the filmsMenu function with the choiceMenu mainSongsMenu 
    mainMenu = filmsMenu()

     # if the user input is string value 1
    if mainMenu == "1":
       # , then call the function the readfilms file
        readfilms.read_tblFilms()

    elif mainMenu == "2":
        addfilms.insert_tblFilms()

    elif mainMenu == "3":
        updatefilms.update_tblFilms()

    elif mainMenu == "4":
        deletefilms.delete_tblFilms()
    
    elif mainMenu == "5":
        reports.reports()
    
    else:
        # reassign the boolean variable of 'mainProgram' False
        mainProgram = False
input("Enter to quit Films App")#

"""