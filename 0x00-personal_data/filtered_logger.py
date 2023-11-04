#!/usr/bin/env python3
"""
Module for filtering log messages.
"""

from typing import List
import re
import logging


class RedactingFormatter(logging.Formatter):
    """ Redacting Formatter class. """

    REDACTION = "***"
    FORMAT = "[HOLBERTON] %(name)s %(levelname)s %(asctime)-15s: %(message)s"
    SEPARATOR = ";"

    def __init__(self, fields: List[str]):
        super(RedactingFormatter, self).__init__(self.FORMAT)
        self.fields = fields

    def format(self, record: logging.LogRecord) -> str:
        """ Format the log record with redacted fields. """
        for field in self.fields:
            record.msg = re.sub(
                rf"{field}=(.*?){self.SEPARATOR}",
                f"{field}={self.REDACTION}{self.SEPARATOR}",
                record.msg
            )
        return super().format(record)


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
