# Creator: Apurv Manjrekar
# CSE 2050 Mod 2 HW
# Prof: Dr. Kloub

import unittest
from DNA_sequence import Sequence, DNA

class TestSequence(unittest.TestCase):
    def setUp(self):
        self.sequence = Sequence("ATGCA")
        self.sequence2 = Sequence("")
        self.DNA_sequence = DNA("ATGCA")
        self.DNA_sequence2  =DNA("")
    
    def test_get_sequence(self):
        "Test method get_sequence that returns the DNA sequence."
        self.assertEqual(self.sequence.get_sequence(), "ATGCA")
        self.assertEqual(self.sequence2.get_sequence(), "")
    
    def test_calculate_length(self):
        "Test method calculate_length that returns length of DNA sequence"
        self.assertEqual(self.sequence.calculate_length(), 5)
        self.assertEqual(self.sequence2.calculate_length(), 0)

    def test_count_nucleotides(self):
        "Test method count_nucleotides that returns a dictionary of the count of each nucelotide."
        self.assertEqual(self.sequence.count_nucleotides(), {'A': 2, 'T': 1, "C": 1, "G": 1})
        self.assertEqual(self.sequence2.count_nucleotides(), {'A': 0, 'T': 0, "C": 0, "G": 0})
    
    def test_reverse_complement(self):
        "Test method reverse_complement which returns the reverse and complement of orignal sequence."
        self.assertEqual(self.DNA_sequence.reverse_complement(), "TGCAT")
        self.assertEqual(self.DNA_sequence2.reverse_complement(), "")

    def test_find_pattern(self):
        "Test method find_pattern which returns all indices of a given pattern in sequence."
        self.assertEqual(self.DNA_sequence.find_pattern("GC"), [2])
        self.assertEqual(self.DNA_sequence2.find_pattern("T"), [])

    def test_calculate_gc_content(self):
        "Test method calculate_gc_content() which returns the gc content in sequence."
        self.assertEqual(self.DNA_sequence.calculate_gc_content(), 40.0)
        self.assertEqual(self.DNA_sequence2.calculate_gc_content(), 0)

unittest.main()