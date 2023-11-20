# fname    = input("Enter you full name: ")
# address   = input("Enter your address: ")
# interest = input("Enter your interest: ")
# age      =    int(input("Enter your age: "))


# create a dictionary 
dict1 = {"Fullname": "Jane Smith", "Age": 23, "Hobby":"Coding", 1:"Gamer"}

# create a dictionary with keys but no values 
print("dictionary with keys but no values")
userDetails1 = {"fname": "", "address": "", "interest":"", "age":""}
# udate dictioanry keys wih values 
# userDetails1["fname"] = "Some Name"
print(userDetails1)

# # Use key to add values to dictionary 

# userDetails1["fname"] = input("Enter your full name: ")
# userDetails1["address"] = input("Enter your address: ")
# userDetails1["interest"] = input("Enter your interests: ")
# userDetails1["age"] = int(input("Enter age: "))
# print(userDetails1)

# "Extension"
# "Modify"
# "To Do: Task 1: write the input statement to add the remaining values to the userDetails1 dictionary above"

# create a dictionary with no keys and no values 
# print("dictionary with no keys and no values")
# userDetails2 = {}
# dict1Key = input("Enter a  key:")
# userDetails2[dict1Key] = input(f"Enter value for {dict1Key}: ")
# print(userDetails2)
"Make"
"To Do: Task 2: Create a dictionary with no keys as shown below, then write the input statement to add the keys and values."
userDetails3 = {}
numOfkeys = 3
for dictItems in range(numOfkeys):
    aKey = input("Enter key: ")
    aValue = input(f"Enter value for {aKey}: ")
    # add all key value pairs to the dictionary
    userDetails3[aKey]=aValue
print(userDetails3)


