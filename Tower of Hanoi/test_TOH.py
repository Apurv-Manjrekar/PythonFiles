# Creator: Apurv Manjrekar
# CSE 2050 Mod 5 HW
# Prof: Dr. Kloub

import unittest

from TOH import tower_of_hanoi_recursive, tower_of_hanoi_iterative

class test_TOH(unittest.TestCase):
    "Class that tests the TOH file."

    def test_tower_of_hanoi_recursive(self):
        "Tests function tower_of_hanoi_recursive which returns the minimum amount of moves for a given amount of disks."
        self.assertEqual(tower_of_hanoi_recursive(-1, "A", "B", "C"), "Number of disks is less than 1. Please enter a valid number of disks.")
        self.assertEqual(tower_of_hanoi_recursive(0, "A", "B", "C"), "Number of disks is less than 1. Please enter a valid number of disks.")
        self.assertEqual(tower_of_hanoi_recursive(1, "A", "B", "C"), 1)
        self.assertEqual(tower_of_hanoi_recursive(3, "A", "B", "C"), 7)
        self.assertEqual(tower_of_hanoi_recursive(5, "A", "B", "C"), 31)
        self.assertEqual(tower_of_hanoi_recursive(10, "A", "B", "C"), 1023)
        self.assertEqual(tower_of_hanoi_recursive(15, "A", "B", "C"), 32767)
        self.assertEqual(tower_of_hanoi_recursive(20, "A", "B", "C"), 1048575)

    def test_tower_of_hanoi_iterative(self):
        "Tests function tower_of_hanoi_iterative which returns the minimum amount of moves for a given amount of disks."
        self.assertEqual(tower_of_hanoi_iterative(-1, "A", "B", "C"), "Number of disks is less than 1. Please enter a valid number of disks.")
        self.assertEqual(tower_of_hanoi_iterative(0, "A", "B", "C"), "Number of disks is less than 1. Please enter a valid number of disks.")
        self.assertEqual(tower_of_hanoi_iterative(1, "A", "B", "C"), 1)
        self.assertEqual(tower_of_hanoi_iterative(3, "A", "B", "C"), 7)
        self.assertEqual(tower_of_hanoi_iterative(5, "A", "B", "C"), 31)
        self.assertEqual(tower_of_hanoi_iterative(10, "A", "B", "C"), 1023)
        self.assertEqual(tower_of_hanoi_iterative(15, "A", "B", "C"), 32767)
        self.assertEqual(tower_of_hanoi_iterative(20, "A", "B", "C"), 1048575)
        
unittest.main()
