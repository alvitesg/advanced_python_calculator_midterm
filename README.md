Midterm Project Summary
I created a NEW repository from scratch and saved all relevant work in the main branch. Commits show my detailed notes as I enhanced the program to meet the project’s objectives.
Github link: alvitesg/advanced_python_calculator_midterm (github.com)

DESIGN PATTERN

CREATIONAL 
My HistoryManager class leverages a SINGLETON (https://www.geeksforgeeks.org/singleton-method-python-design-patterns/) pattern for managing history using pandas Dataframe. The Singleton pattern ensures that a class has only one instance and provides a global point of access to it. I achieved this through the use of class variables and methods, ensuring repeated calls to HistoryManager().

BEHAVIORAL DESIGN PATTER:

My code leverages a COMMAND DESIGN PATTERN (https://refactoring.guru/design-patterns/command) is used to manage commands by defining command classes, each with an “execute” method and registering them with a command handler. The command design pattern allows encapsulates a request as an object, allowing for parameterization of clients and queues, requests and operations. 

My code also leverages  PLUGIN STRATEGY METHOD (Strategy Method - Python Design Patterns - GeeksforGeeks) to separate commands into separate classes. This design pattern provides flexibility. The Plugin pattern supports the Open/Close Principle of the SOLID (SOLID Principles: Open/Closed Principle - DZone)

"Look Before You Leap" (LBYL) and "Easier to Ask for Forgiveness than Permission" (EAFP)

In my code I leveraged both LBYL  and EAFP. LBYL was used when I felt the code was less likely to work and I leveraged if and else statements. An example of this can be seen in the CommandHandler class when defining execute_command: app/commands/__init__.py. In the same file I used EAFP when I knew if was going to most likely work and leverage try, print, and except exceptions with a printing function. (See def execute_command in app/commands/__init__.py). 

The LBYL is preventative, it searches for the command itself before it executes and EAFP perform the execution of the command and then determines (detective) an error after.

All plugins have LBYL and/or EAFP.

LINK TO VIDEO: https://youtu.be/eIGo1tRMu4U

Core Functionality of the Calculator App

The advanced calculator was implemented leveraging a Read-Eval-Print Loop (REPL) to facilitate the direct interaction with the calculator. The calculator supports arithmetic operations (Add, Subtract, Multiply, and Divide, and Hello command), management of calculation history, and access to extended functionalities through dynamically loaded plugins.

Plugin Systems Applicability

This calculator creates a flexible plugin system to allow seamless integration of new commands or features. This system dynamically loads and integrates plugins without modifying the core application code. This system also includes a REPL "Menu" command to list all available plugin commands, ensuring user discoverability and interaction.

The calculator leverages Pandas to manage a robust calculation history, enabling users to access history records through the REPL interface.

History Management

The code leverages a centralized history management process, where there is one single, consistent history of calculations across the application. Using Singleton ensures that all parts of the application contribute to and access the same history.

This setup uses a RotatingFileHandler to ensure that the log files rotate when they reach a specified size, keeping the disk usage in check. Logging messages are formatted to include the timestamp, logger name, log level, and message. Logging is configured to write both to a file (for persistence) and to the console (for immediate feedback during development or monitoring). This approach provides a centralized and flexible logging mechanism, making it easy to log messages from anywhere in your application using Python's built-in logging module.

Logging
I am using the LoggingUtility plugin which provides a comprehensive solution for initializing and using a logging system within my app. It utilizes Python's built-in logging module along with a RotatingFileHandler to ensure that the log files are rotated once they reach a certain size, preventing the log files from consuming too much disk space. The key features of this capability are log rotation, log levels, console logging, format customization.  Link: app/plugins/logging_utility/__init__.py

Dynamic logs can be seen being registered every time a command is run and the app is opened as such.
2024-03-29 23:37:16,073 - root - ERROR - Errors need to be checked
2024-03-29 23:37:16,073 - root - WARNING - Run tests again
2024-03-29 23:37:16,073 - root - CRITICAL - prioritize these tests
