import unittest
import my_date

class MyDateTest(unittest.TestCase):

    def test_is_leap_year1(self):
        self.assertTrue(my_date.is_leap_year(1984))

    def test_is_leap_year2(self):
        self.assertFalse(my_date.is_leap_year(1985))

    def ordinal_date(self):
        self.assertEqual(1,my_date.ordinal_date(1997, 1, 1)) 

    def ordinal_date(self):
        self.assertEqual(32,my_date.ordinal_date(1995, 2, 1))     

    def days_elapsed(self):
        self.assertEqual(1,my_date.days_elapsed(1997, 1, 1, 1997, 1, 2))   

    def days_elapsed(self):
        self.assertEqual(31,my_date.days_elapsed(1997, 1, 1, 1997, 2, 1))    

    def days_elapsed(self):
        self.assertEqual(14,my_date.days_elapsed(1997, 1, 1, 1997, 1, 15))  

    def days_of_week(self):
        self.assertEqual('Monday',my_date.days_of_week(1753, 1, 1))  

    def days_of_week(self):
        self.assertEqual('Saturday',my_date.days_of_week(2023, 9, 29))   

    def to_str(self):
        self.assertEqual('Monday, 08 October 2023',my_date.to_str(2023, 10, 8))        



if __name__ == '__main__':
    unittest.main()