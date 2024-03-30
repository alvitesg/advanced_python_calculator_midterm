"""tests commands init and history .py files"""
# pylint: disable=line-too-long, missing-module-docstring, missing-class-docstring, trailing-whitespace, missing-function-docstring, function-redefined

import unittest
from unittest.mock import MagicMock
from app.commands import CommandHandler, AddRecordCommand, ClearHistoryCommand 
from app.commands import DeleteHistoryCommand, LoadHistoryCommand
from app.calculation_history import CalculationHistory
# from app.commands import history_command

class TestCommands(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        # Initialize CalculationHistory and CommandHandler
        cls.calc_history = CalculationHistory()
        cls.command_handler = CommandHandler()

        # Register commands with the CommandHandler
        cls.command_handler.register_command("add", AddRecordCommand(cls.calc_history))
        cls.command_handler.register_command("clear", ClearHistoryCommand(cls.calc_history))
        cls.command_handler.register_command("delete", DeleteHistoryCommand(cls.calc_history))
        cls.command_handler.register_command("load", LoadHistoryCommand(cls.calc_history))

    def test_command_registration(self):
        """Test that commands are registered correctly."""
        self.assertIn("add", self.command_handler.commands)
        self.assertIn("clear", self.command_handler.commands)
        self.assertIn("delete", self.command_handler.commands)
        self.assertIn("load", self.command_handler.commands)

    def test_register_single_command(self):
        """Test registering a single command."""
        mock_command = MagicMock()
        self.command_handler.register_command("mock", mock_command)
        self.assertIn("mock", self.command_handler.commands, "Mock command should be registered")
        self.assertIs(self.command_handler.commands["mock"], mock_command, "Registered command should match the mock command")

    def setUp(self):
        # Ensure a fresh start for each test by clearing the history
        self.calc_history.clear_history()

    def test_add_command(self):
        self.command_handler.execute_command("add", "2 + 2", "4")
        self.assertIn("2 + 2", self.calc_history.history_df['Calculations'].values, "The operation should be added to history")

    def test_clear_command(self):
        self.command_handler.execute_command("add", "2 + 2", "4")
        self.command_handler.execute_command("clear")
        self.assertTrue(self.calc_history.history_df.empty, "History should be cleared")

    def test_add_command(self):
        self.command_handler.execute_command("add", "4 + 4", "8")
        self.command_handler.execute_command("clear")
        self.assertTrue(self.calc_history.history_df.empty, "History should be cleared")

    def test_delete_command(self):
        self.command_handler.execute_command("add", "2 + 2", "4")
        self.command_handler.execute_command("delete", "0")
        self.assertTrue(self.calc_history.history_df.empty, "History should be empty after deleting the record")

if __name__ == "__main__":
    unittest.main()
    
class TestAddRecordCommandWithArguments(unittest.TestCase):
    def test_add_record_command_with_arguments(self):
        mock_calculation_history = MagicMock()
        add_command = AddRecordCommand(mock_calculation_history)
        operation, result = "5 + 5", "10"
        add_command.execute(operation, result)

        mock_calculation_history.add_record.assert_called_once_with(operation, result)

if __name__ == "__main__":
    unittest.main()
