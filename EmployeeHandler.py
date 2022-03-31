class EmployeeHandler:
    def __init__(self, listEmployees):
        self.listEmployees = listEmployees

    def showMeetingEmployees(self):
        for i in range(len(self.listEmployees)):
            for j in range(i + 1, len(self.listEmployees)):
                print(self.listEmployees[i].compare(self.listEmployees[j]))


