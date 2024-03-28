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
            return pd.read_csv(self.history_file_path)
        else:
            os.makedirs(os.path.dirname(self.history_file_path), exist_ok=True)
            return pd.DataFrame(columns=['Operation', 'Operand1', 'Operand2', 'Result'])

    @classmethod
    def add_record(cls, operation, operand1, operand2, result):
        instance = cls()  # Ensure instance is initialized
        new_record = pd.DataFrame({'Operation': [operation], 'Operand1': [operand1], 'Operand2': [operand2], 'Result': [result]})
        instance._history_df = pd.concat([instance._history_df, new_record], ignore_index=True)
        instance._save_history_to_csv()

    def _save_history_to_csv(self):
        """Saves the history DataFrame to a CSV file."""
        self._history_df.to_csv(self.history_file_path, index=False)
