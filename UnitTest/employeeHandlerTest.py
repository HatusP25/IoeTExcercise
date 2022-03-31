import unittest

from Employee import Employee
from EmployeeHandler import EmployeeHandler


class employeeHandlerTest(unittest.TestCase):

    def test_showMeetingEmployees(self):
        employeeList = [Employee("RENE", "MO10:00-12:00,TU10:00-12:00,TH01:00-03:00,SA14:00-18:00,SU20:00- 21:00"),
                        Employee("ASTRID", "MO10:00-12:00,TH12:00-14:00,SU20:00-21:00")]
        self.assertEqual(EmployeeHandler(employeeList).showMeetingEmployees(), "result.txt")
        employeeList = [Employee("RENE", "MO10:00-12:00,TU10:00-12:00,TH01:00-03:00,SA14:00-18:00,SU20:00- 21:00")]
        self.assertRaises(ValueError, EmployeeHandler(employeeList).showMeetingEmployees)


if __name__ == '__main__':
    unittest.main()
