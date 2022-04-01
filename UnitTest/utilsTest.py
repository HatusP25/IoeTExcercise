import unittest
import utilFunctions

class utilsTest(unittest.TestCase):

    def test_meetingEmployees(self):
        self.assertEqual(utilFunctions.meetingEmployees("../data.txt"), "result.txt")
        self.assertRaises(ValueError, utilFunctions.meetingEmployees, "../nonexists.txt")


if __name__ == "__main__":
    unittest.main()
