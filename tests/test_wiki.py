from func_packages.wiki_func.wikipedia_help import *
import unittest


class TestsCases(unittest.TestCase):
    def setUp(self):
        self.test_data_requests = ['Russia', 'Main_Page', 'Andha_Naal']
        self.wrong_data = 'sidufhgoisuhfg'

    def test_link(self):
        for index in self.test_data_requests:
            self.assertTrue(getting_link(index), True)

    def another_test(self):
        self.assertFalse(getting_link(self.wrong_data), True)


if __name__ == '__main__':
    unittest.main()
