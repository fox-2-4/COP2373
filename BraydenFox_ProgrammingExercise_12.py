
import csv
import numpy as np


def get_exam_grades(fp: str) -> list[list[int]]:
    grades = []
    with open(fp, newline='') as csvfile:
        reader = csv.DictReader(csvfile)
        next(reader)  # skip header row
        for row in reader:
            grades.append([
                int(row["exam_1"]),
                int(row["exam_2"]),
                int(row["exam_3"])
            ])
    return grades


def main():

    file_path = "grades.csv"
    grades = get_exam_grades(file_path)
    pass_threshold = 60
    grades_np = np.array(grades)

    # exam scores on a per-exam basis
    print("Statistics on a per-exam basis:")
    for i in range(grades_np.shape[1]):     # 1d shape
        exam_scores = grades_np[:, i]       # Numpy column slicing
        print(f"Data for exam {i + 1}:")
        print(f"-- Mean:    {np.mean(exam_scores):.2f}")
        print(f"-- Median:  {np.median(exam_scores):.2f}")
        print(f"-- Std dev: {np.std(exam_scores):.2f}")
        print(f"-- Min:     {np.min(exam_scores)}")
        print(f"-- Max:     {np.max(exam_scores)}")

    # overall exam scores factoring in everything
    all_exam_scores = grades_np.flatten()  # flatten array to compute overall stats
    print()
    print("Overall exam statistics:")
    print(f"Mean:    {np.mean(all_exam_scores):.2f}")
    print(f"Median:  {np.median(all_exam_scores):.2f}")
    print(f"Std dev: {np.std(all_exam_scores):.2f}")
    print(f"Min:     {np.min(all_exam_scores)}")
    print(f"Max:     {np.max(all_exam_scores)}")

    # computing pass/fail numbers & percentages
    print(f"Number of students who passed/failed per exam (pass >= {pass_threshold}):")
    nof_students = grades_np.shape[0]  # number of rows is number of students
    for i in range(grades_np.shape[1]):
        exam_scores = grades_np[:, i]                       # for each column
        pass_ct = np.sum(exam_scores >= pass_threshold)     # get count on comparison operation
        fail_ct = nof_students - pass_ct                    # fail count is remainder
        print(f"Exam {i + 1}: {pass_ct} passed; {fail_ct} failed.")

    # calculate overall percentages
    nof_exam_scores = grades_np.size
    total_pass_ct = np.sum(grades_np >= pass_threshold)
    pass_percentage = (total_pass_ct / nof_exam_scores) * 100
    print()
    print(f"Pass percentage: {pass_percentage:.2f}%")



if __name__ == "__main__":
    main()
