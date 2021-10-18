from django.test import TestCase

# Create your tests here.
class DummyTestCase(TestCase):

    
    def test_dummy_test_case(self):
        x = 1
        y = 2
        z = x + y
        self.assertEqual(z, 3)
