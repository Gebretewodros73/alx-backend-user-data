#!/usr/bin/env python3
"""
Module for filtering log messages.
"""

from typing import List
import re


def filter_datum(fields: List[str], redaction: str,
                 message: str, separator: str) -> str:
    """
    Obfuscates specified fields in a log message.

    Args:
        fields: List of strings representing fields to obfuscate.
        redaction: String representing the redaction value.
        message: String representing the log line.
        separator: String representing the character separating fields.

    Returns:
        Obfuscated log message.
    """
    for field in fields:
        pattern = rf"{field}=(.*?){separator}"
        message = re.sub(pattern, f"{field}={redaction}{separator}", message)
    return message


if __name__ == "__main__":
    fields = ["password", "date_of_birth"]
    messages = [
        "name=egg;email=eggmin@eggsample.com;"
        "password=eggcellent;date_of_birth=12/12/1986;",
        "name=bob;email=bob@dylan.com;password=bobbycool;"
        "date_of_birth=03/04/1993;"
    ]

    for message in messages:
        print(filter_datum(fields, 'xxx', message, ';'))