# ACME SCHEDULE EXERCISE
##**Problem:**
The following problem consists in determining how many times have a pair of employees coincided at the office on a 
certain day, given a .txt file which contains the schedules of all employees.

##Proposed solution:
The proposed solution utilizes an Object-Oriented approach, which uses primarily the `Employee` class, which contains
most of the logic surrounding the problem. This class, is created by passing two parameters to the constructor `Name` and `Schedule`,
data which is previously parsed from the input file. Then, the class internally utilizes the `makeSchedule()` method to organize the data 
in a dictionary data structure, for easier access.
<br><br>
In order to solve the problem, the first step is to determine under which circumstances
two different employees coincide at the office. To do this, various methods were explored, however it was found that checking if the check-in hour of any 
employee is inside the range of the hours worked by the other employee (e.g. 10:00-12:00, the range would be 10,11,12) was the most effective way, due to the fact 
that it minimizes the number of comparisons needed to determine if they coincided or not. Furthermore, in order to reduce the time complexity of the solution, 
only the days in which both employees attended to the office are considered, this is obtained using Sets intersections. 
<br><br>
Finally, with all of this in mind, in order to obtain the final solution, the program iterates over every employee, comparing its schedule 
to the next employee's schedule, and write each result to the output file `result.txt`; method that is implemented by the `EmployeeHandler` class in order 
to make the code scalable, and SOLID compliant.


##**Requirements to run the program:**
* You must have installed python 3.5 or greater.
* Clone the project from [GitHub](https://github.com/HatusP25/IoeTExcercise.git)
* Open a terminal at the folder where the project is located
* Run the following command to execute the program: `python main.py data.txt`

**Note:If you wish to use a different set of data, replace data.txt with the 
 path of the file you wish to use.**


##Output:
The output with the results will be found in the same directory as the main program
in a file named "results.txt"
