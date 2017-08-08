"""
Given a CSV file containing the gradebook data from bCourses, prints a data
frame containing the section averages and standard deviations for the specified
assignment.

Command line input should be as follows:
python sectionComp.py path_to_data assignment

Parameters:
path_to_data: path to CSV file containing gradebook
assigment: name of assigment(s), separated by whitespace
"""

import sys
import pandas as pd
import numpy as np

NUM_SECTIONS = 13
MAX_STUDENTS = 35

"""
Returns a data frame containing the scores of students for the given assignment
categorised by sections. The columns are the sections section.
"""
def sectionScores(data, assignment):
    # removing row containing possible points and storing
    possible_pts = data.ix[0]
    data = data.drop(0, axis=0)

    # replace -1 hw scores with 0
    data = data.replace(-1, 0)

    # name of assignment as stored in gradebook
    col_name = None
    for column in data.columns:
        if assignment.lower() in column.lower():
            col_name = column
            break
    if not col_name:
        return("Assignment " + assignment + " not found!")

    df = pd.DataFrame(np.zeros((MAX_STUDENTS, 0)))

    for i in range(1, NUM_SECTIONS):
        num = 100 + i
        section = "STAT 134 DIS " + str(num) + " and STAT 134 LEC 001"
        subset = data[data['Section'] == section]
        score = subset[col_name]
        score.index = range(len(score))
        df[num] = score

    return df

"""
Given a data frame containing student scores categorised by sections (in
columns), returns a data frame giving the mean and standard deviation of each
section.
"""
def collate(df):
    df = pd.DataFrame([df.mean(), df.std()], index=['mean', 'std'])
    df = df.transpose()
    return df

"""
Given a data frame containing student scores categorised by sections (in
columns), returns a list containing the assignment number and section numbers
for which grades have not been uploaded.
"""
def missing(df):
    return pd.isnull(df).all(0).nonzero()[0] + 101

if __name__ == "__main__":
    args = sys.argv
    data_file = args[1]
    assignments = list(args[2:])

    data = pd.read_csv(data_file, sep=",")

    frames = []
    not_uploaded = {}
    for assignment in assignments:
        frame = sectionScores(data, assignment)
        frames.append(frame)
        missing_grades = missing(frame)
        # Check if grades are missing for this assignment
        if missing_grades != []:
            not_uploaded[assignment] = missing_grades
        # Check if assignment can't be found
        if isinstance(frame, str):
            print(frame)
            sys.exit()

    df = pd.concat(frames)
    df = collate(df)

    print("===")
    print("Section Comparison for " + str(assignments))
    print(df)
    print("===")
    if not_uploaded:
        print("Warning! Grades for the following assignments and sections have not been uploaded:")
        for assignment in not_uploaded.keys():
            print(assignment + ":" + str(not_uploaded[assignment]))
