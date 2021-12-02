from system_resources.system_resources import SystemResources
from .canvas_config import CanvasConfig
from .cpu_statistics import CPUStatistics
from .disk_statistics import DiskStatistics
from .memory_statistics import MemoryStatistics
from .networking_statistics import NetworkingStatistics

from matplotlib.backends.backend_qtagg import FigureCanvasQTAgg
from matplotlib.figure import Figure

from typing import List


class Statistics(FigureCanvasQTAgg):
    def __init__(self):
        self._figure = Figure()
        # self._figure.suptitle('Resource Monitor')

        self._resources: List[SystemResources] = list()

        self._cpu_stats = CPUStatistics(self._figure)
        self._disk_stats = DiskStatistics(self._figure)
        self._memory_stats = MemoryStatistics(self._figure)
        self._networking_stats = NetworkingStatistics(self._figure)

        super(Statistics, self).__init__(self._figure)

    def add_resource(self, resource: SystemResources) -> None:
        if CanvasConfig.MAX_SECONDS_ON_PLOTS == len(self._resources):
            self._resources = self._resources[1:]
        self._resources.append(resource)

    def calculate(self) -> None:
        self._cpu_stats.calculate([
            resource.cpu
            for resource in self._resources
        ])
        self._disk_stats.calculate([
            resource.disk
            for resource in self._resources
        ])
        self._memory_stats.calculate([
            resource.memory
            for resource in self._resources
        ])
        self._networking_stats.calculate([
            resource.networking
            for resource in self._resources
        ])

    def clear(self) -> None:
        self._cpu_stats.clear()
        self._disk_stats.clear()
        self._memory_stats.clear()
        self._networking_stats.clear()
