from Employee import Employee
from EmployeeHandler import EmployeeHandler

ListEmployees = []
with open("data.txt", mode="r") as data:
    ListEmployees.extend(
        list((map(lambda line: Employee(line.split("=")[0], line.split("=")[1].strip()), data.readlines())))
    )

handler = EmployeeHandler(ListEmployees)
handler.showMeetingEmployees()
