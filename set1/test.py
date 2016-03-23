import unittest
from set1 import add_absolute_value, multiply_two_largest_numbers, fizz_buzz

class TestSet1(unittest.TestCase):

    def test_add_absolute_value(self):
        for i in range(-5, 5):
            for j in range(-5, 5):
                self.assertEqual(add_absolute_value(i, j), i + abs(j))

    def test_multiply_two_largest_numbers(self):
        
        def multiply_largest(*args):
            """Must have 2+ args"""
            sorted_args = sorted(args, reverse=True)
            return sorted_args[0] * sorted_args[1]

        for i in range(-10, 10):
            for j in range(-10, 10):
                for k in range(-10, 10):
                    self.assertEqual(
                            multiply_two_largest_numbers(i, j, k),
                            multiply_largest(i, j, k)
                            )

    def test_fizz_buzz(self):

        def fizz_buzz_ref(n):
            answer = ""
            if n % 3 == 0:
                answer += "Fizz"
            if n % 5 == 0:
                answer += "Buzz"
            return answer

        for n in range(1, 400):
            self.assertEqual(fizz_buzz, fizz_buzz_ref)

if __name__ == '__main__':
    unittest.main()



