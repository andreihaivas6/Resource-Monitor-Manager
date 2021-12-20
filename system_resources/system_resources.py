from .cpu_resources import CPUResources
from .disk_resources import DiskResources
from .memory_resources import MemoryResources
from .networking_resources import NetworkingResources

import time
import json

from datetime import datetime


class SystemResources:
    def __init__(self) -> None:
        self._time: int = int(time.time()) + 2 * 60 * 60
        self._cpu_resources: CPUResources = CPUResources()
        self._disk_resources: DiskResources = DiskResources()
        self._memory_resources: MemoryResources = MemoryResources()
        self._networking_resources: NetworkingResources = NetworkingResources()

    @property
    def time(self) -> int:
        return self._time

    @property
    def datetime(self) -> str:
        return str(datetime.fromtimestamp(self._time))

    @property
    def cpu(self) -> CPUResources:
        return self._cpu_resources

    @property
    def disk(self) -> DiskResources:
        return self._disk_resources

    @property
    def memory(self) -> MemoryResources:
        return self._memory_resources

    @property
    def networking(self) -> NetworkingResources:
        return self._networking_resources

    def __str__(self) -> str:
        return json.dumps({
            "_time": self.time,
            "_datetime": self.datetime,
            "_cpu_resources": self.cpu.__dict__,
            "_disk_resources": self.disk.__dict__,
            "_memory_resources": self.memory.__dict__,
            "_networking_resources": self.networking.__dict__,
        }, indent=4)
