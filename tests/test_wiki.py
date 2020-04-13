from func_packages.wiki_func.wikipedia_help import *
import unittest


class TestsCases(unittest.TestCase):
    def setUp(self):
        self.test_data_requests = ['Russia', 'Main_Page', 'Andha_Naal']

    def test_link(self):
        for request in self.test_data_requests:
            getting_link(request)


if __name__ == '__main__':
    unittest.main()
