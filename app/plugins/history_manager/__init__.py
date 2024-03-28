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
