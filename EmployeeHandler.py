class EmployeeHandler:
    def __init__(self, listEmployees):
        self.listEmployees = listEmployees

    def showMeetingEmployees(self):
        try:
            if len(self.listEmployees) <= 1:
                raise ValueError
            with open("result.txt", "w") as f:
                for i in range(len(self.listEmployees)):
                    for j in range(i + 1, len(self.listEmployees)):
                        f.write(f'{self.listEmployees[i].compare(self.listEmployees[j])}\n')

            return "result.txt"
        except ValueError:
            raise

