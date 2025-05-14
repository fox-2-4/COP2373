

def main():
    TOTAL_NOF_TICKETS = 20
    MAX_TICKETS_PER_BUYER = 4

    curr_nof_tickets = TOTAL_NOF_TICKETS
    qty_per_buyer: list = []

    while curr_nof_tickets > 0:

        curr_qty = 0
        curr_max_qty = min(MAX_TICKETS_PER_BUYER, curr_nof_tickets)

        while True:
            print(f"Tickets remaining: {curr_nof_tickets}")
            curr_qty = input("> Enter the desired number of tickets to purchase: ")
            if not curr_qty.isdigit():
                print("Invalid input. Please enter a valid number.")
                continue
            curr_qty = int(curr_qty)
            if curr_qty == 0 or curr_qty > curr_max_qty:
                print(f"Invalid amount. Please enter a nonzero amount less than or equal to [{curr_max_qty}].")
                continue
            break

        qty_per_buyer.insert(-1, curr_qty)
        curr_nof_tickets -= curr_qty

    print("All tickets have been sold.")
    print(f"Total number of buyers: {len(qty_per_buyer)}.")


if __name__ == "__main__":
    main()