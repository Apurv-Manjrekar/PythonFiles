# Creator: Apurv Manjrekar
# CSE 2050 Mod 7 HW
# Prof: Dr. Kloub

import unittest

from magic_sort import linear_scan, reverse_list, insertionsort, mergesort, magicsort

class TestMagicSort(unittest.TestCase):

    def test_linear_scan(self):
        "Test method linear_scan which returns the appropriate method of sorting to use on a given list."

        self.assertEqual(linear_scan([]), "Sorted")
        self.assertEqual(linear_scan([0]), "Sorted")
        self.assertEqual(linear_scan([-5]), "Sorted")
        self.assertEqual(linear_scan([0, 1, 2, 2, 4, 5]), "Sorted")
        self.assertEqual(linear_scan([-7, -4, 3, 12, 31]), "Sorted")
        self.assertEqual(linear_scan([12, 10, 9, 7, 2]), "Reversed")
        self.assertEqual(linear_scan([1, -7, -11, -12, -15]), "Reversed")
        self.assertEqual(linear_scan([-5, -7, -11, -18, -22]), "Reversed")
        self.assertEqual(linear_scan([1, 4, 3, 7, 2]), "Insertion")
        self.assertEqual(linear_scan([0, -1, 3, -5, 2]), "Insertion")
        self.assertEqual(linear_scan([2, -5, -6, -8, -9, 2, -8]), "Insertion")
        self.assertEqual(linear_scan([0, 4, -5, 21, -3, -12, -14, 2, 4, 5, 10, 14, -1]), "Insertion")
        self.assertEqual(linear_scan([4, -9, -11, -14, -17, 5, -10, -11]), "Mergesort")
        self.assertEqual(linear_scan([0, -1, 5, -1, -2, 2, -7, -8, 1, -9, 12, -3]), "Mergesort")
        self.assertEqual(linear_scan([-4, -5, -6, 12, -19, -20, 21, -14, -11, -5, -8]), "Mergesort")
        self.assertEqual(linear_scan([0, 5, 1, 12, 8, 7, 4, 13, 0, -5, -12, 7, 8]), "Mergesort")

    def test_reverse_list(self):
        "Test method reverse_list which returns the reversed version of a given list."

        self.assertEqual(reverse_list([]), [])
        self.assertEqual(reverse_list([5]), [5])
        self.assertEqual(reverse_list([10, 5, 2, 1, 0]), [0, 1, 2, 5, 10])
        self.assertEqual(reverse_list([-8, -9, -121, -123, -222]), [-222, -123, -121, -9, -8])
        self.assertEqual(reverse_list([5, 3, 1, -5, -12, -13]), [-13, -12, -5, 1, 3, 5])
        self.assertEqual(reverse_list([12, 14, 151, 512, 234, 654, 67, 86, 12, -54 , -4, -24, -32]), [-32, -24, -4, -54, 12, 86, 67, 654, 234, 512, 151, 14, 12])

    def test_insertionsort(self):
        "Test method insertionsort which returns the sorted version of a given list using insertion sort."
        self.assertEqual(insertionsort([]), [])
        self.assertEqual(insertionsort([0, 4, 2 ,4, 5, 3]), [0, 2, 3, 4, 4, 5])
        self.assertEqual(insertionsort([-5, -4, -8, -12, -2, -1]), [-12, -8, -5, -4, -2, -1])
        self.assertEqual(insertionsort([12, -12, 14, -7, 11, -8, 12]), [-12, -8, -7, 11, 12, 12, 14])
        self.assertEqual(insertionsort([-12, 4, -8, -13, -14, -15, -16, -25, 4, 12]), [-25, -16, -15, -14, -13, -12, -8, 4, 4, 12])
        self.assertEqual(insertionsort([4, 8, -5, 0, -12, -11, 3, 12, 32, 123, -142]), [-142, -12, -11, -5, 0, 3, 4, 8, 12, 32, 123])
    
    def test_mergesort(self):
        "Test method mergesort which returns the sorted version of a given list using merge sort."

        self.assertEqual(mergesort([]), [])
        self.assertEqual(mergesort([4, 6, 12, 4, 3, 6, 12, 2, 5, 12, 5]), [2, 3, 4, 4, 5, 5, 6, 6, 12, 12, 12])
        self.assertEqual(mergesort([-5, -8, -2, -12, -9, -10, -5, -6, -8, -9]), [-12, -10, -9, -9, -8, -8, -6, -5, -5, -2])
        self.assertEqual(mergesort([-1, -5, -12, -14, 0, -5, -3, 12]), [-14, -12, -5, -5, -3, -1, 0, 12])
        self.assertEqual(mergesort([-3, 12, -5, -7, 14, -8, -9, 2, 4, 7]), [-9, -8, -7, -5, -3, 2, 4, 7, 12, 14])
        self.assertEqual(mergesort([5, -7, -8, 2, -4, 5, -3, -12, 4, -131]), [-131, -12, -8, -7, -4, -3, 2, 4, 5, 5])

    def test_magicsort(self):
        "Test method magicsort which returns the sorted version of a given list using the recommended method for that list."

        self.assertEqual(magicsort([], "Sorted"), [])
        self.assertEqual(magicsort([0, 1, 2, 3, 5], "Sorted"), [0, 1, 2, 3, 5])
        self.assertEqual(magicsort([-10, -8, -6, -5, -1], "Sorted"), [-10, -8, -6, -5, -1])
        self.assertEqual(magicsort([-7, -4, -1, 0, 2, 5, 8, 9], "Sorted"), [-7, -4, -1, 0, 2, 5, 8, 9])
        self.assertEqual(magicsort([10, 8, 7, 2, 1], "Reversed"), [1, 2, 7, 8, 10])
        self.assertEqual(magicsort([-1, -5, -8, -12, -14, -17], "Reversed"), [-17, -14, -12, -8, -5, -1])
        self.assertEqual(magicsort([9, 4, 1, -1, -5, -6, -12], "Reversed"), [-12, -6, -5, -1, 1, 4, 9])
        self.assertEqual(magicsort([2, -5, -7, 0, 4, -5], "Insertion"), [-7, -5, -5, 0, 2, 4])
        self.assertEqual(magicsort([10, -2, -5, -8, 4, 2, 3, -1], "Insertion"), [-8, -5, -2, -1, 2, 3, 4, 10])
        self.assertEqual(magicsort([8, 7, -5, -3, 4, 7, 2, -1, -12, -14, 5, 2, 0], "Insertion"), [-14, -12, -5, -3, -1, 0, 2, 2, 4, 5, 7, 7, 8])
        self.assertEqual(magicsort([3, 2, 5, -2, -3, -4, 5, 8, -112, -7, -9], "Mergesort"), [-112, -9, -7, -4, -3, -2, 2, 3, 5, 5, 8])
        self.assertEqual(magicsort([2, 4, 3, 5, 7, 8, 3, 5, 2, 1, 0, 2, 1], "Mergesort"), [0, 1, 1, 2, 2, 2, 3, 3, 4, 5, 5, 7, 8])
        self.assertEqual(magicsort([-1, -2, 5, -2, -3, -4, 6, -7, -8, 2, -1, 3, 1], "Mergesort"), [-8, -7, -4, -3, -2, -2, -1, -1, 1, 2, 3, 5, 6])

unittest.main()