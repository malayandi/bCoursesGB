"""
Merges the gradebook exported from Gradescope with the gradebook exported from
bCourses, readying the new gradebook to be exported to bCourses.

Command line input should be as follows:
python sectionComp.py path_to_BCdata path_to_GSdata assignment remove_blank

Parameters:
path_to_BCdata: path to CSV file containing bCourse gradebook
path_to_GSdata: path to CSV file containing Gradescope gradebook
assigment: name of assigment(s), separated by whitespace
remove_blank: optional Boolean argument; if True, will remove all blank
assignments in final merged gradebook. If not specified, will default to False.
"""

import sys
import sys
import pandas as pd
import numpy as np

"""
Cleans the bCourses gradebook:
1. Removes all summary columns
2. Converts -1 HW scores to 0
3. Removes row of possible points
"""
def bcClean(data):
    possible_pts = data.ix[0]

    # remove summmary columns
    possible_pts = data.ix[0]
    columns = data.columns
    to_keep = []
    for column in columns:
        if "read only" not in str(possible_pts[column]):
            to_keep.append(column)
    data = data[to_keep]
    # convert -1 HW scores to 0
    data = data.replace(-1, 0)
    # drop row of possible points
    data = data.drop(0, axis=0)

    return data

"""
Cleans the gradescope assignment gradebook by removing all columns except
student ID and total score.
Requires that the student IDs are stored in a column labelled SID.
"""
def gsClean(data):
    data = data[["SID", "Total Score"]]
    data["SID"] = pd.to_numeric(data["SID"], errors="coerce")
    return data

"""
Merges the clean gradescope assignment gradebook into the bCourses gradebook.

assignment: name of assignment for which the gradescope gradebook is given
remove_blank: removes blank assignments if True
"""
def merge(bc_data, gs_data, assignment, remove_blank=False):
    col_name = None
    for column in bc_data.columns:
        if assignment.lower() in column.lower():
            col_name = column
            break
    bc_data = bc_data.merge(gs_data, how="left", left_on="SIS User ID", right_on="SID")
    bc_data[col_name] = bc_data["Total Score"]
    bc_data.drop(["SID", "Total Score"], axis=1, inplace=True)
    if remove_blank:
        bc_data.dropna(axis=1, how="all", inplace=True)
    return bc_data

if __name__ == "__main__":
    remove_blank = False
    args = sys.argv
    bc_data_file = args[1]
    gs_data_file = args[2]
    assignment = args[3]
    if len(args) > 4:
        remove_blank = True

    bc_data = pd.read_csv(bc_data_file, sep=",")
    gs_data = pd.read_csv(gs_data_file, sep=",")

    bc_data = bcClean(bc_data)
    gs_data = gsClean(gs_data)

    merged = merge(bc_data, gs_data, assignment, remove_blank)
    merged.to_csv("merged.csv", na_rep=0)
