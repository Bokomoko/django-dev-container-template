from django.test import TestCase

# Create your tests here.


class Test(TestCase):
    # should get a list of BANCOS from the bancos.py file
    def test_get_bancos(self):
        from . import BANCOS

        self.assertEqual(len(BANCOS), 6)
        self.assertEqual(BANCOS[0]['nome'], "Banco do Brasil")


# should run the tests
if __name__ == '__main__':
    import unittest
    unittest.main()
