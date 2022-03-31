from Employee import Employee
from EmployeeHandler import EmployeeHandler


def meetingEmployees(inputPath):
    ListEmployees = []
    try:
        with open(inputPath, mode="r") as data:
            ListEmployees.extend(
                list((map(lambda line: Employee(line.split("=")[0], line.split("=")[1].strip()), data.readlines())))
            )
            handler = EmployeeHandler(ListEmployees)
            return handler.showMeetingEmployees()
    except FileNotFoundError:
        raise ValueError("File not found: %s" % inputPath)


