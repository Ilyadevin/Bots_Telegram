from func_packages.translation_YA.translation import get_translate
import pytest
import time


class TestSuite(pytest):
    def setup(self):
        self.test_case = {'text': 'text', 'language': 'ru'}

    def resource_setup(self, module_to_test):
        print('Prepare the test')
        module_to_test.addfinalizer(get_translate(self.test_case['text'], self.test_case['language']))


if __name__ == '__main__':
    TestSuite().resource_setup()
