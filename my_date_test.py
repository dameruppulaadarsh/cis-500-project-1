import unittest
import my_date

class MyDateTest(unittest.TestCase):

    def test_is_leap_year1(self):
        self.assertTrue(my_date.is_leap_year(1984))

    def test_is_leap_year2(self):
        self.assertFalse(my_date.is_leap_year(1985))

    def ordinal_date(self):
        self.assertEqual(my_date.ordinal_date(2023, 1, 1)) 

    def days_elapsed(self):
        self.assertEqual(my_date.days_elapsed(2023, 1, 1, 2045, 9, 23))   

    def days_of_week(self):
        self.assertEqual(my_date.days_of_week(2022, 3, 12))       

if __name__ == '__main__':
    unittest.main()