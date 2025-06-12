# COP 2373 Programming Exercise 3
# Brayden Fox 06/12/25

from functools import reduce


def main():

    # define expense type for linter type hints (project scope falls short of needing an object)
    exp = tuple[str, float, str]  # (exp_type, exp_amount, exp_formatted)

    # index constants into exp type
    _TYPE = 0
    _AMT = 1
    _FMTD = 2

    # list stores all the expense data entered by the user
    expenses: list[exp] = []

    dollar_fmt = "${:,.2f}"  # global format string

    # main program start
    print("\n--- Monthly Expense Analyzer ---")
    print("\nINSTRUCTIONS:")
    print("Please enter both the expense \'type\' and amount (only the number) separated by a comma, and then [ENTER].")
    print("For example: \"Utilities, 240\"")
    print("When finished entering data, press [ENTER] again to see results.\n")

    # boolean is true while the user elects to enter more expense data
    is_entering: bool = True
    while is_entering:

        # get a line of text from the user
        line: str = input("> ")

        # determine whether user has elected to end data entry
        if len(line) != 0:

            # split the line by the first comma only;
            # produces [exp_type, exp_amt] which is subsequently unpacked by the assignment operation
            # exp_type is stripped of leading/trailing whitespace;
            # exp_amt attempts to parse to a float (and raises ValueError on failure)
            # formatted dollar amount is generated and stored at the same time to avoid having to do it later.
            try:
                exp_type, exp_amount = line.split(",", 1)
                exp_type = exp_type.strip()
                exp_amount = float(exp_amount)
                exp_formatted = dollar_fmt.format(exp_amount)

            # ValueError is raised when coerce to float has failed
            # advise the user and abort appending bad data to expenses list via continue
            except ValueError:
                print(">>> ERROR: unsupported entry format, please try again.")
                print(">>> (Example entries: \"Rent, 1700\", \"Groceries, 265.50\", etc.)")
                continue

            # data is good & parsed correctly; add to list
            expenses.append((exp_type, exp_amount, exp_formatted))

        # user has elected to stop entering data
        else:
            is_entering = False

    print("END OF ENTRY.")

    if len(expenses) != 0:
        # begin calculations of entered data
        # calculate column widths for data table
        # uses a lambda key that checks the length of the appropriate tuple-wise element in the expenses list
        type_col_width: int = len(max(expenses, key=lambda x: len(x[_TYPE]))[_TYPE]) + 1
        fmtd_col_width: int = len(max(expenses, key=lambda x: len(x[_FMTD]))[_FMTD]) + 1

        # ensure column widths are at least as wide as the headers
        type_col_width = max(type_col_width, 5)
        fmtd_col_width = max(fmtd_col_width, 7)

        # sort the expenses in ascending order
        # passes a lambda key so that sorting is performed against the numeric amounts
        expenses = sorted(expenses, key=lambda x: x[_AMT])

        # defines a nested function that, using the computed column widths above, returns a formatted row of data
        # exists to avoid repetition of the same format string throughout the code.
        def format_row(t, f) -> str:
            return f"{t:<{type_col_width}}{f:>{fmtd_col_width}}"

        # print table header & bar
        # utilizes the nested format_row() function to format each text row
        print("\nEXPENSE ANALYSIS:\n")
        print(format_row("Type", "Amount"))
        print("-" * (type_col_width + fmtd_col_width))
        for expense in expenses:
            print(format_row(expense[_TYPE], expense[_FMTD]))

        # use the reduce method to generate the sum total
        # because the function call to reduce is given an initial value, the second parameter of the lambda
        # function (x1) will always be one of the elements of expenses (a tuple of (exp_type, exp_amt, exp_fmtd)),
        # while x0 starts with the initial amount and will thereafter always be a numeric type.
        # Therefore, x1 (the element of expenses) is indexed to access the numeric amount.
        print("")
        expenses_total = reduce(lambda x0, x1: x0 + x1[_AMT], expenses, 0)
        print(f"TOTAL: {dollar_fmt.format(expenses_total)}")

        # the highest/lowest amounts are simply the last/first elements respectively of expenses
        # because the list was sorted
        print(f"HIGHEST: \"{expenses[-1][_TYPE]}\", {expenses[-1][_FMTD]}")
        print(f"LOWEST: \"{expenses[0][_TYPE]}\", {expenses[0][_FMTD]}")

    else:
        print("\nNO DATA GIVEN.")


# call the main function
if __name__ == "__main__":
    main()
