from abc import ABC, abstractmethod


class ILogger(ABC):
    @abstractmethod
    def write(self, log_message: str) -> None:
        ...

class Calculator:
    def __init__(self, logger: ILogger) -> None:
        self.__logger = logger

    def add(self, a: int, b: int) -> int:
        self.__logger.write(f"Adding {a} and {b}")
        return a + b
    

class StdOutLogger(ILogger):
    def __init__(self, log_source: str) -> None:
        self._log_source = log_source

    def write(self, log_message: str) -> None:
        print(f"[{self._log_source}] {log_message}")

class TextLogger(ILogger):
    def __init__(self, log_source: str, file_name: str) -> None:
        self._log_source = log_source
        self._log_file = open(file_name, 'a') # In production-code we need rotating file/folder

    def write(self, log_message: str) -> None:
        self._log_file.write(f"[{self._log_source}] {log_message}")