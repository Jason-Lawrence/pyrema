import unittest

from pyrema import base


class TestBase(unittest.TestCase):

    def test_container_constructor(self):
        title = "This is a Test."
        test = base.Container(title)

        self.assertEqual(test.title, title)

    
