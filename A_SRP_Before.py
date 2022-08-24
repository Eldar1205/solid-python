from __future__ import annotations
from enum import Enum

class Calculator:
    def __init__(self, lt: LoggerType, log_name: str) -> None:
        self._log_type = lt

        if self._log_type == LoggerType.TEXT_FILE:
            self._log_file = open(log_name, 'a') # In production-code we need rotating file/folder
        else:
            self._log_source = log_name

    def add(self, a: int, b: int) -> int:
        log_message = f"Adding {a} and {b}"

        if self._log_type == LoggerType.TEXT_FILE:
            self._log_file.write(log_message)
        else:
            print(f"[{self._log_source}] {log_message}")

        return a + b

class LoggerType(Enum):
    STDOUT = 1
    TEXT_FILE = 2