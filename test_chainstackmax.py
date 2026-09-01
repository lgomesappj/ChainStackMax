# test_chainstackmax.py
"""
Tests for ChainStackMax module.
"""

import unittest
from chainstackmax import ChainStackMax

class TestChainStackMax(unittest.TestCase):
    """Test cases for ChainStackMax class."""
    
    def test_initialization(self):
        """Test class initialization."""
        instance = ChainStackMax()
        self.assertIsInstance(instance, ChainStackMax)
        
    def test_run_method(self):
        """Test the run method."""
        instance = ChainStackMax()
        self.assertTrue(instance.run())

if __name__ == "__main__":
    unittest.main()
