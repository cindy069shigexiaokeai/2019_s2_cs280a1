'''
upi: xgao069
name: Xinyi Gao
student ID: 429784284
'''
import unittest
from drones import Drone, DroneStore

class DroneTest(unittest.TestCase):
    def test_add_success(self):
        #arrange
        dr = Drone("Test drone",  class_type = 1)
        store = DroneStore()
        #act
        actual = store.add(dr)
        #assert
        self.assertIn(dr.id, store._drones)
        #task1 1.Unit test for add() that ensures a drone is successfully added
    def test_add_exception(self):
        #arrange
        dr = Drone("Test drone",  class_type = 1)
        store = DroneStore()
        #act
        actual =  store.add(dr)
        #assert
        with self.assertRaises(Exception): store.add(dr)
         #task1 2.Unit test for add() that checks the method raises an exception if the drone already exists in the store
    def test_remove_success(self):
        #arrange
        dr = Drone("Test drone", class_type=1)
        store = DroneStore()
        #act
        actual = store.add(dr)
        actual = store.remove(dr)
        #assert
        self.assertNotIn(dr.id, store._drones)
        #task1 3. Unit test for remove() that removes an existing drone from the store
    def test_remove_exception(self):
        #arrange
        dr = Drone("Test drone", class_type=1)
        store = DroneStore()
        #assert
        with self.assertRaises(Exception): store.remove(dr)
        #task1 4. Unit test for remove() that checks the method raises an exception if the drone does not exist in the store
if __name__ == '__main__':
    unittest.main()
