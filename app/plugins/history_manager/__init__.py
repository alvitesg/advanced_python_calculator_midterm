# app/plugins/history_manager/__init__.py

import os
import pandas as pd
from dotenv import load_dotenv

class HistoryManager:
    _instance = None
    _initialized = False
    _history_df = pd.DataFrame(columns=['Operation', 'Operand1', 'Operand2', 'Result'])

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super(HistoryManager, cls).__new__(cls)
        return cls._instance

    def __init__(self):
        if not self._initialized:
            self._initialize()
            self.__class__._initialized = True

    def _initialize(self):
        load_dotenv()
        self.history_file_path = os.getenv('HISTORY_FILE_PATH', './data/calculation_history.csv')
        self._history_df = self._load_or_initialize_history()

    def _load_or_initialize_history(self):
        if os.path.exists(self.history_file_path):
            self._history_df = pd.read_csv(self.history_file_path)
        else:
            os.makedirs(os.path.dirname(self.history_file_path), exist_ok=True)
            self._history_df = pd.DataFrame(columns=['Operation', 'Operand1', 'Operand2', 'Result'])

    def _save_history_to_csv(self):
        """Save the history Dataframe to a CSV File."""
        self.history_df.to_csv(self.history_file_path, index=False)

    @classmethod
    def _record_operation(cls, operation, operand1, operand2, result):
        """A generic method to record an operation to the history DataFrame."""
        instance = cls()  # Ensure instance is initialized
        new_record = pd.DataFrame({
            'Operation': [operation], 
            'Operand1': [operand1], 
            'Operand2': [operand2], 
            'Result': [result]
        })
        instance._history_df = pd.concat([instance._history_df, new_record], ignore_index=True)
        instance._save_history_to_csv()

    @classmethod
    def add_record(cls, operand1, operand2, result):
        cls._record_operation("Add", operand1, operand2, result)

    @classmethod
    def subtract_record(cls, operand1, operand2, result):
        cls._record_operation("Subtract", operand1, operand2, result)

    @classmethod
    def multiply_record(cls, operand1, operand2, result):
        cls._record_operation("Multiply", operand1, operand2, result)

    @classmethod
    def divide_record(cls, operand1, operand2, result):
        cls._record_operation("Divide", operand1, operand2, result)

    def _save_history_to_csv(self):
        """Saves the history DataFrame to a CSV file."""
        self._history_df.to_csv(self.history_file_path, index=False)

    @classmethod
    def load_history(cls):
        """Loads the history from the CSV file into the DataFrame."""
        instance = cls()  # Ensures an instance is created following the Singleton pattern
        try:
            instance._history_df = pd.read_csv(instance.history_file_path)
            print("History loaded successfully.")
        except FileNotFoundError:
            print("No history file found. Starting with an empty history.")
            instance._history_df = pd.DataFrame(columns=['Operation', 'Operand1', 'Operand2', 'Result'])
        except Exception as e:
            print(f"An error occurred while loading the history: {e}")
    
    #clear the record from history
    def clear_history(self):
        self.history_df = pd.DataFrame(columns=['Calculations'])
        self._save_history_to_csv()
        print("History cleared successfully.")

    #delete the record from history at a specific index
    def delete_history(self, index):
        if not os.path.exists(self.history_file) or self.history_df.empty:
            return False  # Indicates no action was taken
        if index < 0 or index >= len(self.history_df):
            raise KeyError(f"Invalid index: {index}")
        self.history_df = self.history_df.drop(index).reset_index(drop=True)
        self.save_history()
        return True
    