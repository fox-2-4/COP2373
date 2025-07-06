import csv


def main():
    file_name = "grades.csv"
    # use a context manager to open and read the file
    with open(file_name, newline='') as csvfile:
        reader = csv.DictReader(csvfile)
        field_names = reader.fieldnames
        rows = list(reader)

    # stores column widths for final output table
    col_widths: dict[str: int] = {}

    # compute column widths
    # insert field names into list of rows to factor them in for the column widths
    rows.insert(0, {k: k for k in field_names})
    for field_name in field_names:
        col_widths[field_name] = max([
            len(str(item)) for item in
            [row[field_name] for row in rows]
        ])

    # returns a row of formatted table data.
    def fmt_row(row: dict[str: any]) -> str:
        return " | ".join(f"{item:<{col_widths[field_name]}}" for field_name, item in row.items())

    # display the CSV file in table format
    print()
    print(fmt_row(rows[0]))
    print("-+-".join("-" * w for w in col_widths.values()))
    for row in rows[1:]:
        print(fmt_row(row))


if __name__ == "__main__":
    main()