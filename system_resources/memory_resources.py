import psutil
import json


class MemoryResources:
    def __init__(self) -> None:
        """
        Get information about Memory resources
        """
        memory = psutil.virtual_memory()

        self._total_memory: int = memory.total
        self._available_memory: int = memory.available
        self._used_memory: int = memory.used
        self._used_memory_percent: float = round(memory.percent, 1)
        self._available_memory_percent: float = round(self.available_memory / self.total_memory * 100, 1)

    @property
    def total_memory(self) -> int:
        return self._total_memory

    @property
    def available_memory(self) -> int:
        return self._available_memory

    @property
    def used_memory(self) -> int:
        return self._used_memory

    @property
    def used_memory_percent(self) -> float:
        return self._used_memory_percent

    @property
    def available_memory_percent(self) -> float:
        return self._available_memory_percent

    def __str__(self) -> str:
        """
        Return resources in dictionary format in order to be easy to read.
        :return: string containing all the information
        """
        return json.dumps(self.__dict__, indent=4)
