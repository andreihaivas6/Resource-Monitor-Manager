from system_resources.system_resources import SystemResources
from .cpu_statistics import CPUStatistics
from .disk_statistics import DiskStatistics
from .memory_statistics import MemoryStatistics
from .networking_statistics import NetworkingStatistics

from matplotlib.backends.backend_qtagg import FigureCanvasQTAgg
from matplotlib.figure import Figure

from typing import List


class Statistics(FigureCanvasQTAgg):
    def __init__(self, system_resources: List[SystemResources] = None):
        figure = Figure()

        self._cpu_stats = CPUStatistics(figure)
        self._disk_stats = DiskStatistics(figure)
        self._memory_stats = MemoryStatistics(figure)
        self._networking_stats = NetworkingStatistics(figure)

        super(Statistics, self).__init__(figure)
