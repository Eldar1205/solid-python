from __future__ import annotations
from enum import Enum

class Calculator:
    def __init__(self) -> None:
        self.__logger = Logger(LoggerType.TEXT_FILE, "calculator_log.txt")

    def add(self, a: int, b: int) -> int:
        self.__logger.write(f"Adding {a} and {b}")
        return a + b
    

class Logger:
    def __init__(self, lt: LoggerType, log_name: str) -> None:
        self._log_type = lt

        if self._log_type == LoggerType.TEXT_FILE:
            self._log_file = open(log_name, 'a') # In production-code we need rotating file/folder
        else:
            self._log_source = log_name

    def write(self, log_message: str) -> None:
        if self._log_type == LoggerType.TEXT_FILE:
            self._log_file.write(log_message)
        else:
            print(f"[{self._log_source}] {log_message}")

class LoggerType(Enum):
    STDOUT = 1
    TEXT_FILE = 2