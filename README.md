# bCoursesGB
**bCoursesGB** is a set of tools designed to help educators process and analyze grade books as exported from bCourses easily. Designed to simplify and streamline the process of analyzing data from bCourses' clunky grade book, bCoursesGB allows instructors to spend less time dealing with administrative issues and more time teaching.

## sectionComp
**sectionComp** is a simple utility designed to help instructors quickly and painlessly compare student performance across all discussion sections. Once called, sectionComp prints a table containing the mean and standard deviations of all section for a specified assignment.

### Usage:
Download the file `sectionComp.py`. Once downloaded, simply run the following command:

	python sectionComp.py path_to_data assignment

### Parameters:
* path_to_data: The path to the CSV file of the grade book as exported from bCourses
* assignment: The name of the assignment(s) to be used for comparison (in quotation marks); separate assignments by whitespace.


## gs2bcExport
**gs2bcExport** is a simple utility designed to help integrate grades from a Gradescope grade book into a bCourses grade book. Once called, gs2bcExport creates a new grade book, “merged.csv”, containing the merged grades, and which can be directly uploaded to bCourses.

Currently, gs2bcExport can only merge assignments from Gradescope one at a time i.e. to merge multiple assignments, run the script repeatedly on each Gradescope assignment’s grade book.


### Usage:
Download the file `gs2bcExport`. Once downloaded, simply run the following command:

	python sectionComp.py path_to_BCdata path_to_GSdata assignment remove_blank

### Data Formatting Requirements
The Gradescope grade book must contain a column named “SID” containing Student IDs of each student.

### Parameters:
* path_to_BCdata: path to CSV file containing bCourse gradebook
* path_to_GSdata: path to CSV file containing Gradescope gradebook
* assigment: name of assigment(s), separated by whitespace
* remove_blank: optional Boolean argument; if True, will remove all non-graded assignments in final merged gradebook. If not specified, will default to False and leave those assignments in.


## Requests/Contributors

If you would like a specific utility to be developed or want to contribute to developing utilities for bCoursesGB, please reach out.