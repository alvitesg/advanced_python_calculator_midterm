# advanced_python_calculator_midterm

# Core Functionality of the Calculator
# The advanced calculator was implemented leveraging a Read-Eval-Print Loop (REPL) to facilitate the direct interaction with the calculator. The calculator supports arithmetic operations (Add, Subtract, Multiply, and Divide, and Hello command), management of calculation history, and access to extended functionalities through dynamically loaded plugins.

# Plugin Systems Applicability
# This calculator creates a flexible plugin system to allow seamless integration of new commands or features. This system dynamically loads and integrates plugins without modifying the core application code. This system also includes a REPL "Menu" command to list all available plugin commands, ensuring user discoverability and interaction.

# The calculator leverages Pandas to manage a robust calculation history, enabling users to load, save, clear, and delete history records through the REPL interface.

# A. Short description and link to your implememtation of the design patterns you use
# The design pattern being used in the HistoryManager class, as described in the modifications and usage context provided, is the # 
# Singleton Pattern. The Singleton Pattern ensures that a class has only one instance and provides a global point of access to it. This 
# pattern is particularly useful when exactly one object is needed to coordinate actions across the system.

'''Centralized History Management: There should be a single, consistent history of calculations across the application. Using a singleton ensures that all parts of the application contribute to and access the same history.

Resource Efficiency: By ensuring only one instance of the HistoryManager exists, the application conserves resources, avoiding unnecessary duplication of the history data.

Simplified Access: The Singleton Pattern simplifies how different parts of the application access and record calculation history, providing a clear and consistent interface.'''

# B. Description of how you used environment variables and link to your code to illustrate.

# C. Explain and link to how you are using logging.

# D. link to and explain how you are using try/catch / exceptions to illustrate "Look Before You Leap" (LBYL) and "Easier to Ask for Forgiveness than Permission" (EAFP)/

# E. Create a 3-5 minute video demonstration of using the calculator, highlighting its key features and functionalities. Link the video to the repository readme.

# F. Other
