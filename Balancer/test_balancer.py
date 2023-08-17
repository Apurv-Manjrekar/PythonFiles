import unittest
from Balancer import ParenthesesBalancer

class TestBalancer(unittest.TestCase):
    "Class that tests the ParenthesesBalancer Class"
    
    def setUp(self):
        "Sets up ParenthesesBalancer variables for testing."
        self.balancer = ParenthesesBalancer()
        self.balancer1 = ParenthesesBalancer()
        self.balancer2 = ParenthesesBalancer()
        self.balancer3 = ParenthesesBalancer()
        self.balancer4 = ParenthesesBalancer()
        self.balancer5 = ParenthesesBalancer()
        self.balancer6 = ParenthesesBalancer()
        self.balancer7 = ParenthesesBalancer()
        self.balancer8 = ParenthesesBalancer()
        self.balancer9 = ParenthesesBalancer()
        self.balancer10 = ParenthesesBalancer()
        self.balancer11 = ParenthesesBalancer()
        self.balancer12 = ParenthesesBalancer()
        self.balancer10.push("(")
        self.balancer10.push("{")
        self.balancer11.push("ACE{d")

    def test_is_balanced(self):
        "Tests the is_balanced() method that returns true or false based on if the given string is balanced."
        self.assertEqual(self.balancer.is_balanced("()"), True)
        self.assertEqual(self.balancer1.is_balanced("("), False)
        self.assertEqual(self.balancer2.is_balanced("]"), False)
        self.assertEqual(self.balancer3.is_balanced("{()}"), True)
        self.assertEqual(self.balancer4.is_balanced("{(}"), False)
        self.assertEqual(self.balancer5.is_balanced("{()"), False)
        self.assertEqual(self.balancer6.is_balanced("()}"), False)
        self.assertEqual(self.balancer7.is_balanced("AB{CVE(CSK[dsd]SF)c}SF"), True)
        self.assertEqual(self.balancer8.is_balanced("AB{CVE(CSK[dsd)SF]c}SF"), False)

    def test_is_empty(self):
        "Tests the is_empty() method that returns true if the stack is empty and false otherwise."
        self.assertEqual(self.balancer9.is_empty(), True)
        self.assertEqual(self.balancer10.is_empty(), False)
        self.assertEqual(self.balancer11.is_empty(), False)

    def test_push(self):
        "Tests the push() method that adds the given element to the stack and returns nothing."
        self.assertEqual(self.balancer10.push("{"), None)
        self.assertEqual(self.balancer10.push(""), None)
        self.assertEqual(self.balancer10.push("AA"), None)

    def test_pop(self):
        "Tests the pop() method that removes and returns the top element in the stack."
        self.assertEqual(self.balancer10.pop(), "{")
        self.assertEqual(self.balancer12.pop(), None)

    def test_peek(self):
        "Tests the peek() method that returns the top element in the stack."
        self.assertEqual(self.balancer10.peek(), "{")
        self.assertEqual(self.balancer12.peek(), None)

unittest.main()