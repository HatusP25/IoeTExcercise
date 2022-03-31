import unittest

from Employee import Employee


class employeesTest(unittest.TestCase):

    def test_compare(self):
        emp = Employee("RENE", "MO10:00-12:00,TU10:00-12:00,TH01:00-03:00,SA14:00-18:00,SU20:00- 21:00")
        emp2 = Employee("ASTRID", "MO10:00-12:00,TH12:00-14:00,SU20:00-21:00")
        self.assertEqual(emp.compare(emp2), "RENE-ASTRID:2")
        self.assertRaises(ValueError, emp.compare, "hello")

    def test_makeSchedule(self):
        expectedResult = {'MO': {'start': {'hh': 10, 'mm': 0}, 'end': {'hh': 12, 'mm': 0}},
                          'TH': {'start': {'hh': 12, 'mm': 0}, 'end': {'hh': 14, 'mm': 0}},
                          'SU': {'start': {'hh': 20, 'mm': 0}, 'end': {'hh': 21, 'mm': 0}}}
        emp = Employee("ASTRID", "MO10:00-12:00,TH12:00-14:00,SU20:00-21:00")
        self.assertEqual(emp.schedule, expectedResult)
        self.assertRaises(ValueError,emp.makeSchedule,"MOj0:00-12:00,TH12:00-14:00,SU20:00-21:00")
        self.assertRaises(IndexError,emp.makeSchedule,"MO10-00-12:00,TH12:00-14:00,SU20:00-21:00")


if __name__ == "__main__":
    unittest.main()
