"""
This module contains unittests for the CalculationHistory class.
It tests the functionality of adding, clearing, and deleting records in the calculation history.
"""
import os
import unittest
import pandas as pd
from app.calculation_history import CalculationHistory
# pylint: disable=line-too-long, missing-module-docstring, missing-class-docstring, trailing-whitespace, missing-function-docstring, function-redefined
class TestCalculationHistory(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        """Set up test environment."""
        cls.calc_hist = CalculationHistory()
        # Ensure the test environment is clean by clearing any existing history
        cls.calc_hist.clear_history()

    def test_singleton(self):
        """Test the singleton pattern."""
        another_instance = CalculationHistory()
        self.assertEqual(id(self.calc_hist), id(another_instance), "CalculationHistory should be a singleton")

    def test_clear_history(self):
        """Test clearing the history."""
        self.calc_hist.add_record("3 + 3", "6")
        self.calc_hist.clear_history()
        self.assertEqual(len(self.calc_hist.history_df), 0, "History should be cleared")

    def test_delete_history(self):
        """Test deleting a specific record from history."""
        self.calc_hist.add_record("5 + 5", "10")
        self.calc_hist.add_record("6 + 6", "12")
        delete_success = self.calc_hist.delete_history(0)  # Attempt to delete the first record
        self.assertTrue(delete_success, "Delete operation should succeed")
        self.assertEqual(len(self.calc_hist.history_df), 1, "One record should remain after deletion")
        self.assertNotIn("5 + 5", self.calc_hist.history_df['Calculations'].tolist(), "Deleted operation should not be in history")
    
    def test_add_multiple_records(self):
        self.calc_hist.add_record("1 + 1", "2")
        self.calc_hist.add_record("2 + 2", "4")
        self.assertEqual(len(self.calc_hist.history_df), 2, "Should have two records")

    def test_save_and_load_history(self):
        # Add records to history
        self.calc_hist.add_record("3 + 3", "6")
        self.calc_hist.add_record("6 + 6", "12")

        # Save the history
        self.calc_hist.save_history()

        # Clear the in-memory history dataframe to simulate starting fresh
        self.calc_hist.history_df = pd.DataFrame(columns=['Calculations'])

        # Load the history from CSV
        self.calc_hist.load_history()

        # Verify the records after loading
        self.assertTrue((self.calc_hist.history_df['Calculations'] == "3 + 3").any(), "Record '3 + 3' should exist after loading history")
        self.assertTrue((self.calc_hist.history_df['Calculations'] == "6 + 6").any(), "Record '6 + 6' should exist after loading history")

    @classmethod
    def tearDownClass(cls):
        """Clean up after tests."""
        # Optional: Remove the test CSV file after tests are done
        if os.path.exists(cls.calc_hist.history_file):
            os.remove(cls.calc_hist.history_file)
    
    def test_delete_from_empty_history(self):
        self.calc_hist.clear_history()
        self.assertFalse(self.calc_hist.delete_history(0), "Deleting from empty history should return False")

    def test_delete_invalid_index(self):
        self.calc_hist.add_record("5 + 5", "10")
        with self.assertRaises(KeyError):
            self.calc_hist.delete_history(-1)
        with self.assertRaises(KeyError):
            self.calc_hist.delete_history(100)

    def test_clear_history_after_adding(self):
        self.calc_hist.add_record("6 + 6", "12")
        self.calc_hist.clear_history()
        self.assertTrue(self.calc_hist.history_df.empty, "History should be empty after clearing")

    @classmethod
    def tearDownClass(cls):
        """Clean up after tests."""
        # Optional: Remove the test CSV file after tests are done
        os.remove(cls.calc_hist.history_file)

if __name__ == '__main__':
    unittest.main()
