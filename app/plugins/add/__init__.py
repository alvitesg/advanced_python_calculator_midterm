import sys
from decimal import Decimal, InvalidOperation
from app.commands import Command
from app.commands import CommandHandler
from app.plugins.history_manager import HistoryManager

class addCommand(Command):
    def execute(self, *args):
        """Executes the add command with the provided arguments."""
        if len(args) != 2:
            print("Error: addCommand requires exactly two arguments.")
            return

        try:
            # Convert arguments to Decimal for precision in arithmetic operations
            num1, num2 = map(Decimal, args)
            result = num1 + num2
            # capture the successful addition operation in the history
            HistoryManager.add_record(str(num1), str(num2), str(result)) # "Add" is now internally determined
            print(f"The result of adding {num1} and {num2} is {result}")
        except InvalidOperation:
            print("Error: Invalid arguments. Both arguments must be numbers.")
            # except (ValueError, TypeError) as e:
            # print(f"Error: Invalid arguments. Both arguments must be numbers. Details: {e}")

# This allows the command to be imported directly from the add package
__all__ = ['AddCommand']
