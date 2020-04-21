from func_packages.wiki_func.wikipedia_help import *
import unittest


class TestsCases(unittest.TestCase):
    def setUp(self):
        self.test_data_requests = ['Russia', 'Main_Page', 'Andha_Naal']
        self.wrong_data = 'sidufhgoisuhfg'

    def test_link(self):
        self.assertEqual(self.test_data_requests[1], str())

    def test_case_wrong(self):
        test_case = getting_link(self.wrong_data)
        self.assertEqual(test_case, 'https://en.wikipedia.org/wiki/')


if __name__ == '__main__':
    unittest.main()
