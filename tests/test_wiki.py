from func_packages.wiki_func.wikipedia_help import *
import unittest


class TestsCases(unittest.TestCase):
    def setUp(self):
        self.test_data_requests = ['Russia', 'Main_Page', 'Andha_Naal']
        self.wrong_data = 'sidufhgoisuhfg'

    def test_link(self):
        for request in self.test_data_requests:
            test_case = getting_link(request)
            self.assertEqual(test_case, str())

    def test_case_wrong(self):
        self.assertEqual(getting_link(self.wrong_data), self.wrong_data)


if __name__ == '__main__':
    unittest.main()
