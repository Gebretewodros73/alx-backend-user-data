# 0x00. Personal data

This repository contains a set of tasks related to handling and securing personal data. Each task is outlined below:

## Task 0: Regex-ing

### Description
Write a function called `filter_datum` that obfuscates log messages using regular expressions.

### Arguments
- `fields`: a list of strings representing fields to obfuscate
- `redaction`: a string representing the redaction value
- `message`: a string representing the log line
- `separator`: a string representing the character separating fields in the log line

## Task 1: Log formatter

### Description
Update the `RedactingFormatter` class to accept a list of fields as a constructor argument. Implement the `format` method to filter values in incoming log records using `filter_datum`.

## Task 2: Create logger

### Description
Implement a `get_logger` function that returns a `logging.Logger` object. The logger should be named "user_data" and only log up to `logging.INFO` level. It should not propagate messages to other loggers. It should have a `StreamHandler` with `RedactingFormatter` as the formatter.

## Task 3: Connect to secure database

### Description
Implement a `get_db` function that returns a connector to a secure MySQL database. Use environment variables to obtain credentials.

## Task 4: Read and filter data

### Description
Implement a `main` function that retrieves all rows in the users table from the database and displays each row under a filtered format.

## Task 5: Encrypting passwords

### Description
Implement a `hash_password` function that takes a password string and returns a salted, hashed password using the bcrypt package.

## Task 6: Check valid password

### Description
Implement an `is_valid` function that checks if a provided password matches the hashed password using bcrypt.

## Usage

For detailed instructions on how to run each task, refer to the specific task descriptions and code examples provided.

## Repository Structure

- `0x00-personal_data`
  - `filtered_logger.py`: Contains the implementation for all the tasks.
- `0x01-anonymization`
  - ... (Add similar structure and descriptions for other directories)

## Files

- `main.py`: Example usage of the functions and classes defined in `filtered_logger.py`.
- `main.sql`: SQL script to set up the MySQL database for testing.

## Instructions

Follow the instructions provided in each task to complete the corresponding implementation.

## Ready for manual review

Now that you have completed the tasks, you can submit your work for manual review using the provided link.

**Note**: Reviews are due by November 10, 2023, 6:00 AM.
