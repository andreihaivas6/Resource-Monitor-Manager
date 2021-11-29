import psutil


class MemoryResources:
    def __init__(self):
        memory = psutil.virtual_memory()

        self._total_memory = memory.total
        self._available_memory = memory.available
        self._used_memory = memory.used
        self._user_memory_percent = round(memory.percent, 1)
