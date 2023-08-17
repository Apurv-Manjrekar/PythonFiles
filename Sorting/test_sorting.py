# Creator: Apurv Manjrekar
# CSE 2050 Mod 6 HW
# Prof: Dr. Kloub

import unittest
from sorting import find_zero_index, sort_halfsorted

class TestSortingFunctions(unittest.TestCase):

    def test_find_zero_index(self):
        "Test method find_zero_index which returns the index of the zero within a list."

        #Test a full range of the possible 0 indices for different list lengths
        # Length 0
        lst = []
        self.assertEqual(find_zero_index(lst), -1)
        # Length 1
        lst1 = [0]
        self.assertEqual(find_zero_index(lst1), 0)
        # Length 2
        lst2 = [0, 1]
        self.assertEqual(find_zero_index(lst2), 0)
        # Length 4
        lst3 = [0, 3, 2, 5]
        self.assertEqual(find_zero_index(lst3), 0)
        # Length 12
        lst4 = [0, 3, 5, 1, 2, 5, 3, 4, 6, 2, 9, 10]
        self.assertEqual(find_zero_index(lst4), 0)
        # Length 2
        lst5 = [-3, 0]
        self.assertEqual(find_zero_index(lst5), 1)
        # Length 4
        lst6 = [-3, 0, 5, 3]
        self.assertEqual(find_zero_index(lst6), 1)
        # Length 4
        lst7 = [-6, -12, 0, 2]
        self.assertEqual(find_zero_index(lst7), 2)
        # Length 4
        lst8 = [-6, -12, -8, 0]
        self.assertEqual(find_zero_index(lst8), 3)
        # Length 12
        lst9 = [-9, 0, 4, 6, 2, 7, 1, 8, 3, 6, 4, 11]
        self.assertEqual(find_zero_index(lst9), 1)
        # Length 12
        lst10 = [-8, -12, 0, 23, 4, 10, 5, 12, 2, 4, 1, 12]
        self.assertEqual(find_zero_index(lst10), 2)
        # Length 12
        lst11 = [-14, -11, -2, 0, 1, 4, 1, 7, 201, 3, 7, 1]
        self.assertEqual(find_zero_index(lst11), 3)
        # Length 12
        lst12 = [-2, -5, -4, -6, 0, 2, 4, 5, 6, 44, 4, 101]
        self.assertEqual(find_zero_index(lst12), 4)
        # Length 12
        lst13 = [-9, -4, 7, -9, -6, 0, 4, 42, 12, 4, 8, 7]
        self.assertEqual(find_zero_index(lst13), 5)
        # Length 12
        lst14 = [-32, -10, -14, 15, -2, -8, 0, 1, 14, 2, 78, 21]
        self.assertEqual(find_zero_index(lst14), 6)
        # Length 12
        lst15 = [-12, -52, -11, -13, -14, -7, -1, 0, 2, 7, 2, 12]
        self.assertEqual(find_zero_index(lst15), 7)
        # Length 12
        lst16 = [-2, -5, -7, -3, -4, -7, -7, -6, 0, 45, 123, 10]
        self.assertEqual(find_zero_index(lst16), 8)
        # Length 12
        lst17 = [-321, -32, -6, -312, -76, -98, -12, -35, -4, 0, 4, 11]
        self.assertEqual(find_zero_index(lst17), 9)
        # Length 12
        lst18 = [-323, -23, -4, -87, -72, -123, -3, -93, -2, -45, 0, 102]
        self.assertEqual(find_zero_index(lst18), 10)
        # Length 12
        lst19 = [-2, -4, -32, -21, -24, -53, -89, -4879, -123, -90, -5, 0]
        self.assertEqual(find_zero_index(lst19), 11)

    def test_sort_halfsorted(self):
        "Test method sort_halfsorted which returns the sorted version of the list."

        lst = [-3, -5, -2, 0, 1, 4, 3]
        Lcopy = lst[:] #Make a deep-copy of that list using slicing
        Lcopy.sort()  #Sort the deep-copy list
        sort_halfsorted(lst) #Sort the original list using sort_halfsorted function
        self.assertListEqual(lst, Lcopy) #Compare the orginal list that should be sorted by sort_halfsorted function with the sorted deep-copy
        
        #More test cases to test a list with different lengths

        #Length 0
        lst1 = []
        Lcopy1 = lst1[:]
        Lcopy1.sort()
        sort_halfsorted(lst1)
        self.assertListEqual(lst1, Lcopy1)
        # Length 1
        lst2 = [0]
        Lcopy2 = lst2[:]
        Lcopy2.sort()
        sort_halfsorted(lst2)
        self.assertListEqual(lst2, Lcopy2)
        # Length 2
        lst3 = [0, 1]
        Lcopy3 = lst3[:]
        Lcopy3.sort()
        sort_halfsorted(lst3)
        self.assertListEqual(lst3, Lcopy3)
        # Length 3
        lst4 = [-1, 0, 1]
        Lcopy4 = lst4[:]
        Lcopy4.sort()
        sort_halfsorted(lst4)
        self.assertListEqual(lst4, Lcopy4)
        # Length 4
        lst5 = [-4, -7, 0, 1]
        Lcopy5 = lst5[:]
        Lcopy5.sort()
        sort_halfsorted(lst5)
        self.assertListEqual(lst5, Lcopy5)
        # Length 5
        lst6 = [-7, -8, 0, 7, 4]
        Lcopy6 = lst6[:]
        Lcopy6.sort()
        sort_halfsorted(lst6)
        self.assertListEqual(lst6, Lcopy6)
        # Length 6
        lst7 = [-9, -4, -7, 0, 4, 5]
        Lcopy1 = lst1[:]
        Lcopy1.sort()
        sort_halfsorted(lst1)
        self.assertListEqual(lst1, Lcopy1)
        # Length 7
        lst8 = [-8, -12, -14, 0, 7, 3, 4]
        Lcopy8 = lst8[:]
        Lcopy8.sort()
        sort_halfsorted(lst8)
        self.assertListEqual(lst8, Lcopy8)
        # Length 8
        lst9 = [-12, -10, -4, -1, 0, 2, 3, 5]
        Lcopy9 = lst9[:]
        Lcopy9.sort()
        sort_halfsorted(lst9)
        self.assertListEqual(lst9, Lcopy9)
        # Length 9
        lst10 = [-19, -42, -23, -32, 0, 45, 23, 32, 12]
        Lcopy10 = lst10[:]
        Lcopy10.sort()
        sort_halfsorted(lst10)
        self.assertListEqual(lst10, Lcopy10)
        # Length 10
        lst11 = [-312, -53, -453, -34, -322, 0, 213, 2, 32, 54]
        Lcopy11 = lst11[:]
        Lcopy11.sort()
        sort_halfsorted(lst11)
        self.assertListEqual(lst11, Lcopy11)
        # Length 11
        lst12 = [-45, -231, -43, -65, -87, 0, 231, 43, 657, 324, 90]
        Lcopy12 = lst12[:]
        Lcopy12.sort()
        sort_halfsorted(lst12)
        self.assertListEqual(lst12, Lcopy12)
        # Length 12
        lst13 = [-35, -352, -21, -32, 0, 412, 42, 64, 757, 412, 35]
        Lcopy13 = lst13[:]
        Lcopy13.sort()
        sort_halfsorted(lst13)
        self.assertListEqual(lst13, Lcopy13)
        # Length 13
        lst14 = [-35, 0, 532, 654, 4212, 74323, 5, 231, 64, 21, 53, 123]
        Lcopy14 = lst14[:]
        Lcopy14.sort()
        sort_halfsorted(lst14)
        self.assertListEqual(lst14, Lcopy14)
        # Length 14
        lst15 = [0, 436, 74, 234, 754, 34, 57, 23, 46, 23, 24, 57, 444]
        Lcopy15 = lst15[:]
        Lcopy15.sort()
        sort_halfsorted(lst15)
        self.assertListEqual(lst15, Lcopy15)
        # Length 15
        lst16 = [-432, -342, -54, -641, -35, -53, -65, -12, -80, -213, -23, 0, 142, 35]
        Lcopy16 = lst16[:]
        Lcopy16.sort()
        sort_halfsorted(lst16)
        self.assertListEqual(lst16, Lcopy16)
        # Length 16
        lst17 = [-463, -43, -34, -65, -76, -1, -32, -64, -31, -12, -35, -123, -124, -2, -47, 0]
        Lcopy17 = lst17[:]
        Lcopy17.sort()
        sort_halfsorted(lst17)
        self.assertListEqual(lst17, Lcopy17)

unittest.main()

