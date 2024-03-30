from app.commands.history_command import BaseCommand
from app.plugins.logging_utility import LoggingUtility
from app.commands import Command
from app.commands import CommandHandler
from app.plugins.history_manager import HistoryManager

class LoadCommand(Command):
    def execute(self, *args):
        # No arguments expected for the load command, but checking to keep consistency
        if len(args) > 0:
            print("Error: The load command does not require any arguments.")
            LoggingUtility.warning("The load command does not require any arguments.")
            return
        else:
            try:
                # Proceed with loading the history
                if HistoryManager.load_history():
                    print("History loaded successfully.")
                    LoggingUtility.info("History loaded successfully.")
                else:
                    print("Error: Unable to load history. Please check the history file.")
                    LoggingUtility.warning("Unable to load history. Please check the history file.")
            except Exception as e:  # Catching any unexpected errors during the load operation
                print(f"Error: An unexpected error occurred - {str(e)}")
                LoggingUtility.error(f"An unexpected error occurred - {str(e)}")

# This allows the command to be imported directly from its package
__all__ = ['LoadCommand']