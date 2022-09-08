"""
sample test using calc
"""

from django.test import SimpleTestCase

from app import calc

class CaldTests(SimpleTestCase):
    """ test the calc module """

    def test_add_numbers(self):
        """ test adding numbers """

        result = calc.add(5, 6)

        self.assertEqual(result, 11)