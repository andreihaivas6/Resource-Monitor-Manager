import psutil


class MemoryResources:
    BYTES_IN_GIGABYTE = 1024 ** 3

    def __init__(self):
        memory = psutil.virtual_memory()

        self._total_memory = round(memory.total / MemoryResources.BYTES_IN_GIGABYTE, 2)
        self._available_memory = round(memory.available / MemoryResources.BYTES_IN_GIGABYTE, 2)
        self._used_memory = round(memory.used / MemoryResources.BYTES_IN_GIGABYTE, 2)
        self._user_memory_percent = memory.percent
