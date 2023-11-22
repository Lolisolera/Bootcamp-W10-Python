#Ticketing Program project practice

#Create a program in python that can simulate a ticketing system for an Adventure Theme Park.
#The python application will ask the user the list of questions below before calculating their total charge.
"""Your program should
	•	Provide a welcome message.
	•	Display the entrance ticket prices.
	•	Ask how many adult tickets are required.
	•	Ask how many child tickets are required.
	•	Ask how many senior citizen tickets are required.
	•	Ask for the lead booker surname (for the ticket)
	•	Ask if they require a parking pass for the car park.
	•	Add the total number of tickets to display the total cost.
	•	Print a ticket (display lead booker surname, tickets purchased, today’s date*)
	•	Print a car parking pass (if requested)
	Use data validation techniques to avoid runtime errors through incorrect data entry. 
	Thank the customer for their purchase.
*You will need to investigate how to add today's date to the ticket. 

Entrance ticket type example
Adult			£20
Child			£12
Senior citizen		£11

Parking
Free (car pass must be displayed/printed if yes is selected)
Design
Use pseudocode to design your program.
Think carefully about what will be needed in the main program and in each subroutine/function.


*You will need to research how to add today's date to the ticket (Hint: import datetime or date). "
import datetime
"""

def calculate_ticket_cost(adult_tickets, child_tickets, senior_tickets):
    adult_price = 20
    child_price = 12
    senior_price = 11

    total_cost = (adult_tickets * adult_price) + (child_tickets * child_price) + (senior_tickets * senior_price)
    return total_cost

def print_ticket(surname, adult_tickets, child_tickets, senior_tickets, parking_pass):
    print("\n----- Adventure Theme Park Ticket -----")
    print(f"Lead Booker: {surname}")
    print(f"Adult Tickets: {adult_tickets}")
    print(f"Child Tickets: {child_tickets}")
    print(f"Senior Citizen Tickets: {senior_tickets}")
    print("Date: ", datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"))
    print("--------------------------------------")

    if parking_pass:
        print("\n----- Parking Pass -----")
        print("Car pass must be displayed.")
        print("-------------------------")

def main():
    print("Welcome to Adventure Theme Park!")
    print("\nEntrance Ticket Prices:")
    print("Adult: £20, Child: £12, Senior Citizen: £11")

    try:
        adult_tickets = int(input("\nHow many adult tickets are required? "))
        child_tickets = int(input("How many child tickets are required? "))
        senior_tickets = int(input("How many senior citizen tickets are required? "))

        surname = input("Enter the lead booker's surname: ")

        parking_pass = input("Do you require a parking pass? (yes/no): ").lower() == 'yes'

        total_cost = calculate_ticket_cost(adult_tickets, child_tickets, senior_tickets)

        print(f"\nTotal Cost: £{total_cost}")

        print_ticket(surname, adult_tickets, child_tickets, senior_tickets, parking_pass)

        print("\nThank you for your purchase! Enjoy your visit to Adventure Theme Park.")
    except ValueError:
        print("Invalid input. Please enter a valid number.")

if __name__ == "__main__":
    main()
