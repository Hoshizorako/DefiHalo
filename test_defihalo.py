# test_defihalo.py
"""
Tests for DefiHalo module.
"""

import unittest
from defihalo import DefiHalo

class TestDefiHalo(unittest.TestCase):
    """Test cases for DefiHalo class."""

    def test_initialization(self):
        """Test class initialization."""
        instance = DefiHalo()
        self.assertIsInstance(instance, DefiHalo)

    def test_run_method(self):
        """Test the run method."""
        instance = DefiHalo()
        self.assertTrue(instance.run())

if __name__ == "__main__":
    unittest.main()
