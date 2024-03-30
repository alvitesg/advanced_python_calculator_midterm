from app.commands.history_command import BaseCommand
from app.plugins.logging_utility import LoggingUtility
from app.commands import Command
from app.commands import CommandHandler
from app.plugins.history_manager import HistoryManager


class DeleteCommand(Command):
    def execute(self, *args):
        #"Look Before You Leap" (LBYL)
        #We have one arguement to be passed for delete command, high chance that user might pass more than one arguement
        if len(args) == 0:
            print("Error: You have to declare an index after the delete command.")
            LoggingUtility.warning("You have to declare an index after the delete command.")
            return
        elif len(args) > 1:
            print("Error: You can declare only one index after the delete command.")
            LoggingUtility.warning("You can declare only one index after the delete command.")
            return
        else:
            try:
                #"Easier to Ask for Forgiveness than Permission" (EAFP)
                #Instead of checking with multiple if else statement to check multiple error, it is easier to use try catch block
                index = int(args[0])
                # Proceed with deletion if the provided index is valid
                if HistoryManager.delete_history(index):
                    print(f"Record at index {index + 1} deleted.")
                    LoggingUtility.warning("Unable to delete record. Please check the index or CSV file.")
                else:
                    print("Error: Unable to delete record. Please check the index or CSV file.")
                    LoggingUtility.info("Record deleted.")
            except ValueError:
                print("Error: Index must be an integer.")
                LoggingUtility.error("Error: Index must be an integer.")

# This allows the command to be imported directly from its package
__all__ = ['DeleteCommand']

                