from app.plugins.logging_utility import LoggingUtility
from app.commands import Command
from app.plugins.history_manager import HistoryManager

class ClearCommand(Command):
    def execute(self, *args):
        # No arguments expected for the clear command, but checking to keep consistency
        if len(args) > 0:
            print("Error: The clear command does not require any arguments.")
            LoggingUtility.warning("The clear command does not require any arguments.")
            return
        else:
            # Obtain the singleton instance of HistoryManager
            history_manager = HistoryManager()
            try:
                # Directly call the instance method clear_history
                history_manager.clear_history()
                print("History cleared successfully.")
                LoggingUtility.info("History cleared successfully.")
            except Exception as e:  # Catching any unexpected errors during the clear operation
                print(f"Error: An unexpected error occurred - {str(e)}")
                LoggingUtility.error(f"An unexpected error occurred - {str(e)}")

# This allows the command to be imported directly from its package
__all__ = ['ClearCommand']
