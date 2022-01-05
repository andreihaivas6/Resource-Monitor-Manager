from system_resources.memory_resources import MemoryResources
from statistics.utils.canvas_config import CanvasConfig
from statistics.utils.utils import Utils

import matplotlib.figure
import matplotlib.axes

from typing import List


class MemoryStatistics:
    def __init__(self, figure: matplotlib.figure.Figure) -> None:
        """
        Create graph plots.
        """
        self._axes: matplotlib.axes.Axes = figure.add_subplot(
            CanvasConfig.NUMBER_ROWS,
            CanvasConfig.NUMBER_COLUMNS,
            CanvasConfig.MEMORY_POSITION
        )

    def calculate(self, resources: List[MemoryResources]) -> None:
        """
        Add plot and text on window
        :param resources: the list of resources from last minute
        :return: None
        """
        self._add_graphs(resources)
        self._add_text()

    def _add_graphs(self, resources: List[MemoryResources]) -> None:
        """
        Add plot on window
        :param resources: the list of resources from last minute
        :return: None
        """
        seconds = Utils.get_seconds()
        memory_percents = Utils.get_front_padding(resources) + [
            resource.used_memory_percent
            for resource in resources
        ]
        memory_percents = memory_percents[::-1]

        Utils.draw_plot(
            self._axes, seconds, memory_percents,
            'purple', 'Memory usage'
        )

    def _add_text(self) -> None:
        """
        Add text on window
        :return: None
        """
        self._axes.set_ylabel('percent (%)')

    def clear(self) -> None:
        """
        Clear window
        :return: None
        """
        self._axes.clear()
