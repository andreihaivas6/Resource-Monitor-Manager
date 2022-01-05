from system_resources.system_resources import SystemResources
from statistics.utils.canvas_config import CanvasConfig
from .cpu_statistics import CPUStatistics
from .disk_statistics import DiskStatistics
from .information import Information
from .memory_statistics import MemoryStatistics
from .networking_statistics import NetworkingStatistics

from matplotlib.backends.backend_qtagg import FigureCanvasQTAgg
from matplotlib.figure import Figure
from typing import List


class Statistics(FigureCanvasQTAgg):
    def __init__(self) -> None:
        """
        Create statistics for all resources on window
        """
        self.figure: Figure = Figure()

        self._resources: List[SystemResources] = list()

        self._cpu_stats: CPUStatistics = CPUStatistics(self.figure)
        self._disk_stats: DiskStatistics = DiskStatistics(self.figure)
        self._memory_stats: MemoryStatistics = MemoryStatistics(self.figure)
        self._networking_stats: NetworkingStatistics = NetworkingStatistics(self.figure)
        self._information: Information = Information(self.figure)

        super(Statistics, self).__init__(self.figure)

    @property
    def current_time(self) -> int:
        """
        Get current time
        :return: current time on int
        """
        return self._resources[-1].time

    def set_resources_from_history(self, resources: List[SystemResources]) -> None:
        """
        Update resources for history usage
        :param resources: the list of resources from last minute
        :return: None
        """
        self._resources = resources

    def clear_resources(self) -> None:
        """
        Clear the resources list
        :return: None
        """
        self._resources.clear()

    def add_resource(self, resource: SystemResources) -> None:
        """
        Add a new resource to list
        :param resource: the list of resources from last minute
        :return: None
        """
        if CanvasConfig.MAX_SECONDS_ON_PLOTS == len(self._resources):
            self._resources = self._resources[1:]
        self._resources.append(resource)

    def calculate(self) -> None:
        """
        Calculate all statistics regarding system resources
        :return: None
        """
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
        self._information.calculate(self._resources)

    def clear(self) -> None:
        """
        Clear the screen
        :return: None
        """
        self._cpu_stats.clear()
        self._disk_stats.clear()
        self._memory_stats.clear()
        self._networking_stats.clear()
        self._information.clear()
