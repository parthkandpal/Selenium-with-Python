import unittest
from employee import Employee
from unittest.mock import patch

class TestEmployee(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        print("setUpClass \n")

    @classmethod
    def tearDownClass(cls):
        print("tearDownClass")

    def setUp(self):
        print("setUp")
        self.emp_1 = Employee("Parth", "Kandpal", 50000)
        self.emp_2 = Employee("User", "Test", 30000)

    def tearDown(self):
        print("tearDown")


    def test_email(self):
        print("test_email")
        self.assertEqual(self.emp_1.email,"Parth.Kandpal@email.com")
        self.assertEqual(self.emp_2.email, "User.Test@email.com")


        self.emp_1.first="john"
        self.emp_2.first="Jane"

        self.assertEqual(self.emp_1.email, "john.Kandpal@email.com")
        self.assertEqual(self.emp_2.email, "Jane.Test@email.com")


    def test_fullname(self):
        print("test_fullname")
        self.assertEqual(self.emp_1.fullname, "Parth Kandpal")
        self.assertEqual(self.emp_2.fullname, "User Test")

        self.emp_1.first = "john"
        self.emp_2.first = "Jane"

        self.assertEqual(self.emp_1.fullname, "john Kandpal")
        self.assertEqual(self.emp_2.fullname, "Jane Test")


    def test_apply_raise(self):
       print("apply raise")
       self.emp_1.apply_raise()
       self.emp_2.apply_raise()


       self.assertEqual(self.emp_1.pay, 52500)
       self.assertEqual(self.emp_2.pay, 31500)


    def test_monthly_schedule(self):
        with patch('employee.requests.get') as mocked_get:
            mocked_get.return_value.ok = True
            mocked_get.return_value.text='Success'

        schedule=self.emp_1.monthly_schedule('May')
        mocked_get.assert_called_with('http://company.com/Kandpal/May')
        self.assertEqual(schedule,'Success')