from abc import ABC, abstractmethod
from app.calculation_history import CalculationHistory

class Command(ABC):
    @abstractmethod
    def execute(self, *args):
        pass

class CommandHandler:
    def __init__(self):
        self.commands = {}

    def register_command(self, command_name: str, command: Command):
        self.commands[command_name] = command
        print(f"Command '{command_name}' registered") #Feedback for debugging

    def execute_command(self, command_name: str, *args):
        """ Look before you leap (LBYL) - Use when its less likely to work
        if command_name in self.commands:
            self.commands[command_name].execute()
        else:
            print(f"No such command: {command_name}")"""
        """Easier to ask for forgiveness than permission (EAFP) - Use when its going to most likely work"""
        try:
            self.commands[command_name].execute(*args)
            print(f"Command '{command_name}' executed with args {args}.")  # Feedback
        except KeyError:
            print(f"No such command: {command_name}")
        except Exception as e:
            print(f"Error executing command '{command_name}': {e}")

if __name__ == "__main__":
    calculation_history = CalculationHistory()
    command_handler = CommandHandler()

    # Register commands
    command_handler.register_command("clear", ClearHistoryCommand(calculation_history))
    command_handler.register_command("delete", DeleteHistoryCommand(calculation_history))
    command_handler.register_command("load", LoadHistoryCommand(calculation_history))

    # Example usage
    command_handler.execute_command("load")  # Load history
    command_handler.execute_command("clear")  # Clear history
    command_handler.execute_command("delete", "0")  # Delete the first record
    
# Command to add a record
class AddRecordCommand(Command):
    def __init__(self, calculation_history):
        self.calculation_history = calculation_history

    def execute(self, operation, result):
        self.calculation_history.add_record(operation, result)
        print("Record added.")

# Command to clear history
class ClearHistoryCommand(Command):
    def __init__(self, calculation_history):
        self.calculation_history = calculation_history

    def execute(self):
        self.calculation_history.clear_history()
        print("History cleared.")

# Command to delete a specific history record
class DeleteHistoryCommand(Command):
    def __init__(self, calculation_history):
        self.calculation_history = calculation_history

    def execute(self, index):
        try:
            index = int(index)  # Ensure index is an integer
            success = self.calculation_history.delete_history(index)
            if success:
                print(f"Record at index {index} deleted.")
            else:
                print("Failed to delete record.")
        except ValueError:
            print("Invalid index provided. Please use a valid integer.")

# Command to load history
class LoadHistoryCommand(Command):
    def __init__(self, calculation_history):
        self.calculation_history = calculation_history

    def execute(self):
        success = self.calculation_history.load_history()
        if success:
            print("History loaded.")
        else:
            print("No history to load.")
