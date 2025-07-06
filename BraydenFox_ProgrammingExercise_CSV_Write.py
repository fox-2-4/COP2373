import csv
from typing import Callable


def main():
    is_debugging = False
    file_name = "grades.csv"                                                    # filename
    field_names = ("first_name", "last_name", "exam_1", "exam_2", "exam_3")     # field names for csv file
    field_types = (str, str, int, int, int)  # needs to be Callable type        # expected field data types

    # manual data entry
    if not is_debugging:
        # stores data to be formatted in csv file
        data: list[dict] = []
        # collect number of expected entries
        nof_entries = int(input("> Please enter the number of student entries: "))
        for entry_idx in range(nof_entries):
            # for the start of each entry, append an empty working dict
            data.append({})
            print(f"Current entry {entry_idx + 1} of {nof_entries}...")
            # for each field of each entry, collect data
            for field_idx, field_name in enumerate(field_names):
                # loop continues while data is not of accepted type
                while True:
                    item = input(f"> Please enter data for \"{field_name}\": ")
                    # validate type of entered data
                    try:
                        item = field_types[field_idx](item)
                        break
                    except (ValueError, TypeError):
                        print(f">>> Invalid type for \"{field_name}\";")
                        print(f">>> Expected: \"{field_types[field_idx]}\".")
                        continue

                data[-1][field_name] = item  # add the data to the current field

    else:
        # test data
        data = [
            {"first_name": "Alice", "last_name": "Johnson", "exam_1": 85, "exam_2": 90, "exam_3": 88},
            {"first_name": "Bob", "last_name": "Smith", "exam_1": 78, "exam_2": 82, "exam_3": 80},
            {"first_name": "Charlie", "last_name": "Davis", "exam_1": 92, "exam_2": 88, "exam_3": 91},
            {"first_name": "Diana", "last_name": "Lee", "exam_1": 88, "exam_2": 84, "exam_3": 89},
            {"first_name": "Ethan", "last_name": "Clark", "exam_1": 74, "exam_2": 76, "exam_3": 79}
        ]

    # create/overwrite file at file_name
    # use the fieldnames tuple and write the header
    with open(file_name, 'w', newline='') as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=field_names)
        writer.writeheader()
        writer.writerows(data)


if __name__ == "__main__":
    main()
