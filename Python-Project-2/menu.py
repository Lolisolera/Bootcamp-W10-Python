
import readrecipes, addrecipes, updaterecipes, deleterecipes, reports

#create function
def menuFile():
    with open('Python-Project-2/recipeBook.txt') as recipeMenuFile:

        #read from menu and assign it to a varaible
        recipeFileData = recipeMenuFile.read()
        return recipeFileData 
    
   
#print(menuFile())

def recipeMenu():
    option = 0 # initialise the option variable with an integer value 0
    optionsList = ["1","2","3","4","5","6"]

    # initialise the menu file function with the choiceMenu variable 
    choiceMenu = menuFile() 

    while option not in optionsList:
        # call/invoke the function though the variable choiceMenu
        print(choiceMenu) # display the options from the menu file

        # re-assign the value of the option variable 
        option = input("Enter an option from the Recipe Book Main menu: ")
        # if user input is not on the list
        if option not in optionsList:
            # do this/execute the code below
            print(f"{option} is not a valid choice! ")
    return option
# print(recipeMenu())

# create a boolean variable 
mainProgram = True

while mainProgram: # while True
    # initialise the recipeMenu function with the choiceMenu mainRecipeMenu 
    mainMenu = recipeMenu()

     # if the user input is string value 1
    if mainMenu == "1":
       # , then call the function the readfilms file
        readrecipes.read_recipeBook()

    elif mainMenu == "2":
        addrecipes.insert_recipeBook()

    elif mainMenu == "3":
        updaterecipes.update_recipeBook()

    elif mainMenu == "4":
        deleterecipes.delete_recipeBook()
    
    elif mainMenu == "5":
        reports.reports()
    
    else:
        # reassign the boolean variable of 'mainProgram' False
        mainProgram = False
input("Press Enter to quit Recipe Book App")#