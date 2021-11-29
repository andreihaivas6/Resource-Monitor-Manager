import psutil
import json


class MemoryResources:
    def __init__(self):
        memory = psutil.virtual_memory()

        self._total_memory = memory.total
        self._available_memory = memory.available
        self._used_memory = memory.used
        self._used_memory_percent = round(memory.percent, 1)

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

    def __str__(self) -> str:
        return json.dumps(self.__dict__, indent=4)
