'''
upi: xgao069
name: Xinyi Gao
student ID: 429784284
'''
import unittest
from drones import Drone, DroneStore
from datetime import date
from operators import Operator, OperatorAction, OperatorStore

class OperatorTest(unittest.TestCase):
     #1.The data for the operator passes all the validation rules.
     def test_add_operator_pass_all_rules(self):
         #arrange
        operatorstore = OperatorStore()
        operator = Operator()
        operator.first_name = "Cindy"
        operator.date_of_birth = date(1998, 2, 3)
        operator.drone_license = 2
        operator.operations = 6
        #act
        actual = operatorstore.add(operator)
        #assert
        self.assertTrue(len( actual.messages) == 0)
        
     #2. Test checking when each validation rule fails (five tests.)
     #1,The operator must have a first name.        
     def test_add_operator_age_wrong(self):
        #arrange
        operatorstore = OperatorStore()
        operator = Operator()
        operator.date_of_birth = date(1998, 2, 3)
        operator.drone_license = 2
        operator.operations = 6
        #act
        actual = operatorstore.add(operator)
        #assert
        self.assertIn("First name is required", actual.messages)

     #2. Test checking when each validation rule fails (five tests.)
     #2,The operator must have a date of birth.

     def test_add_operator_birth_wrong(self):
         #arrange
        operatorstore = OperatorStore()
        operator = Operator()
        operator.first_name = "Cindy"
        operator.drone_license = 2
        operator.operations = 6
        #act
        actual = operatorstore.add(operator)
        #assert
        self.assertIn("Date of birth is required", actual.messages)

       #2. Test checking when each validation rule fails (five tests.)
        #3,The operator must have a drone license.
     def test_add_operator_drone_license(self):
         #arrange
        operatorstore = OperatorStore()
        operator = Operator()
        operator.first_name = "Cindy"
        operator.date_of_birth = date(1998, 2, 3)
        operator.operations = 6
        #act
        actual = operatorstore.add(operator)
        #assert
        self.assertIn("Drone license is required", actual.messages)

         #2. Test checking when each validation rule fails (five tests.)
        #4,To hold a drone class 2 license, the operator must be at least 20 years old.
     def test_add_operator_age_more_than_20(self):
         #arrange
        operatorstore = OperatorStore()
        operator = Operator()
        operator.first_name = "Cindy"
        operator.date_of_birth = date(2000, 2, 3)
        operator.drone_license = 2
        operator.operations = 6
        #act
        actual = operatorstore.add(operator)
        #assert
        self.assertIn("Operator should be at least twenty to hold a class 2 license", actual.messages)

         #2. Test checking when each validation rule fails (five tests.)
         #5,To hold a rescue drone endorsement, the operator must have been involved in five prior rescue operations.
     def test_add_operator_rescue_5(self):
          #arrange
        operatorstore = OperatorStore()
        operator = Operator()
        operator.first_name = "Cindy"
        operator.date_of_birth = date(1998, 2, 3)
        operator.drone_license = 2
        operator.operations = 2
        #act
        actual = operatorstore.add(operator)
        #assert
        self.assertIn("More than 5 rescue operations is required", actual.messages)

        #3. Check that the operator is added to the store.
     def test_add_operator_successfully(self):
         #arrange
        operatorstore = OperatorStore()
        operator = Operator()
        operator.first_name = "Cindy"
        operator.date_of_birth = date(1998, 2, 3)
        operator.drone_license = 2
        operator.operations = 6
        #act
        actual = operatorstore.add(operator)
        #assert
        if actual.is_valid():
            actual.commit() 
        self.assertIn(operator.id, operatorstore._operators)

        #4.check that the operator has been added to the store.
     def test_add_operator_exception(self):
         #arrange
        operatorstore = OperatorStore()
        operator = Operator()
        operator.first_name = "Cindy"
        operator.date_of_birth = date(1998, 2, 3)
        operator.drone_license = 2
        operator.operations = 6
        #act
        actual = operatorstore.add(operator)
        #assert
        if actual.is_valid():
            actual.commit() 
        with self.assertRaises(Exception):actual.commit() 
if __name__ == '__main__':
    unittest.main()
