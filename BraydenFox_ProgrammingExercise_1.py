# COP 2373
# Brayden Fox
# 05/14/25

# This program sells a pre-defined limited number of cinema tickets, where each buyer can buy up to 4 tickets.
# The maximum number of tickets available is 20. The program prompts the user for a desired number of tickets,
# confirms the quantity, and displays the total remaining tickets after the sale. It repeats until all tickets are
# sold, whereby it displays the total number of buyers.


# main program
def main():
    # unchanging program parameters
    TOTAL_NOF_TICKETS = 20
    MAX_TICKETS_PER_BUYER = 4

    # stores the current number of remaining tickets available for purchase
    curr_nof_tickets = TOTAL_NOF_TICKETS

    # stores the quantity purchased by each buyer (the length of the array "stores" the number of buyers)
    qty_per_buyer: list = []

    # main loop
    while curr_nof_tickets > 0:

        # calculate the current maximum number of tickets remaining to be sold on this iteration
        curr_max_qty = min(MAX_TICKETS_PER_BUYER, curr_nof_tickets)

        # loop for input & validation
        while True:
            print(f"Tickets remaining: {curr_nof_tickets}")
            curr_qty = collect_int_from_user()

            # confirm chosen quantity lies within the current acceptable range
            if curr_qty == 0 or curr_qty > curr_max_qty:
                print(f"Invalid amount. Please enter a nonzero amount less than or equal to [{curr_max_qty}].")
                continue
            break

        # append the chosen amount to the quantity-per-buyer array and modify the current number of tickets
        qty_per_buyer.insert(-1, curr_qty)
        curr_nof_tickets -= curr_qty

    # all tickets have been sold; display final output & exit
    print("All tickets have been sold.")
    print(f"Total number of buyers: {len(qty_per_buyer)}.")


# collects and validates user input as a digit string
def collect_int_from_user() -> int:
    while True:
        qty = input("> Enter the desired number of tickets to purchase: ")
        if not qty.isdigit():
            print("Invalid input. Please enter a valid number.")
        else:
            break
    return int(qty)


# calls the main program
if __name__ == "__main__":
    main()