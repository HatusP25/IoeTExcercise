class EmployeeHandler:
    def __init__(self, ListEmployees):
        self.ListEmployees = ListEmployees

    def showMeetingEmployees(self):
        for i in range(len(self.ListEmployees)):
            for j in range(i + 1, len(self.ListEmployees)):
                print(self.ListEmployees[i].compare(self.ListEmployees[j]))


