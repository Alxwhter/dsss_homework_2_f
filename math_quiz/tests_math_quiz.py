import unittest
from math_quiz import random_number, random_mathsymbol, calculate_solution


class TestMathGame(unittest.TestCase):
    """
    Class to Test the function of the Math Game
    """

    def test_random_number(self):
        # Test if random numbers generated are within the specified range
        min_val = 1
        max_val = 10
        for _ in range(1000):  # Test a large number of random values
            rand_num = random_number(min_val, max_val)
            self.assertTrue(min_val <= rand_num <= max_val)
            pass
            
        #Test with two negative Numbers
        min_val = -5
        max_val = -3
        for _ in range(1000):
            rand_num = random_number(min_val,max_val)
            self.assertTrue(min_val <= rand_num <= max_val)
            pass

    def test_random_mathsymbol(self):
        # Test if every symbol is possible
        for _ in range (1000):
            rand_symbol = random_mathsymbol()
            self.assertTrue((rand_symbol == '+') or (rand_symbol == '-') or (rand_symbol == '*'))
            pass

    def test_calculate_solution(self):
            test_cases = [
                (5, 2, '+', '5 + 2', 7),
                (5, 2, '-', '5 - 2', 3),
                (5, 2, '*', '5 * 2', 10),
                (0, 2, '+', '0 + 2', 2),
                (0, 2, '-', '0 - 2', -2),
                (0, 2, '*', '0 * 2', 0)
            ]

            for num1, num2, operator, expected_problem, expected_answer in test_cases:
                PROBLEM, ANSWER = calculate_solution(num1,num2,operator)
                self.assertTrue((PROBLEM == expected_problem) or (ANSWER == expected_answer))
                pass

if __name__ == "__main__":
    unittest.main()
