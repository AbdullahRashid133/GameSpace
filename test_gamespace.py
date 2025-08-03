# test_gamespace.py
"""
Tests for GameSpace module.
"""

import unittest
from gamespace import GameSpace

class TestGameSpace(unittest.TestCase):
    """Test cases for GameSpace class."""
    
    def test_initialization(self):
        """Test class initialization."""
        instance = GameSpace()
        self.assertIsInstance(instance, GameSpace)
        
    def test_run_method(self):
        """Test the run method."""
        instance = GameSpace()
        self.assertTrue(instance.run())

if __name__ == "__main__":
    unittest.main()
