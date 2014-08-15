import unittest

import vtkanim.sources


class TestCase(unittest.TestCase):
    
    def test_generate(self):
        ug = vtkanim.sources.generate()
        self.assertTrue(ug)
