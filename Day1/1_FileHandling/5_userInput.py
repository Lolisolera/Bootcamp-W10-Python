fname    = input("Enter you full name: ")
address   = input("Enter your address: ")
interest = input("Enter your interest: ")
age      =    int(input("Enter your age: "))

"Make"
"To Do: Task 1: Use the code above to ask for user input and then save it to a file called userDetails.txt"

"Method 1"
with open('Week10/Pt7_FilesDictsCodeBase/1_FileHandling/userDetails.txt', 'a') as userData:
    "method 1"
    userData.write(fname + address + interest + str(age))
    userData.write(f"/n{fname}  {address} {interest} {age}")

"Method 2"



"Further reading"
# https://www.w3schools.com/python/python_file_handling.asp