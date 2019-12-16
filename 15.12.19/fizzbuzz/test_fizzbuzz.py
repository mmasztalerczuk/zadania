import io
import unittest
import unittest.mock
from .fizzbuzz import fizzbuzz, call_func_in_given_range, print_elements_of_list


class FizzBuzzTest(unittest.TestCase):
    def test01_simple_test(self):
        # given
        n = 1

        # when
        out = fizzbuzz(n)

        # then
        self.assertEqual(1, out)

    def test02_value_3(self):
        # given
        n = 3

        # when
        out = fizzbuzz(n)

        # then
        self.assertEqual("Fizz", out)

    def test02_value_5(self):
        # given
        n = 5

        # when
        out = fizzbuzz(n)

        # then
        self.assertEqual("Buzz", out)

    def test02_value_15(self):
        # given
        n = 15

        # when
        out = fizzbuzz(n)

        # then
        self.assertEqual("FizzBuzz", out)


class CallFuncTests(unittest.TestCase):
    def test01_simple_test(self):
        # given
        def foo(n):
            return n

        # when
        results = call_func_in_given_range(foo, 1, 101)

        # then
        self.assertEqual([_ for _ in range(1, 101)], results)


class BetterPrintTest(unittest.TestCase):
    @unittest.mock.patch("sys.stdout", new_callable=io.StringIO)
    def test01_simple_test(self, mock_stdout):
        # given
        l = ["aaa", "bbb"]

        # when
        print_elements_of_list(l)

        # then
        self.assertEqual("1 aaa\n2 bbb\n", mock_stdout.getvalue())
