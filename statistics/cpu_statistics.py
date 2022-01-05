from system_resources.cpu_resources import CPUResources
from statistics.utils.canvas_config import CanvasConfig
from statistics.utils.utils import Utils

import matplotlib.figure
import matplotlib.axes

from typing import List


class CPUStatistics:
    def __init__(self, figure: matplotlib.figure.Figure) -> None:
        """
        Create graph plots.
        """
        self._axes: matplotlib.axes.Axes = figure.add_subplot(
            CanvasConfig.NUMBER_ROWS,
            CanvasConfig.NUMBER_COLUMNS,
            CanvasConfig.CPU_POSITION
        )

    def calculate(self, resources: List[CPUResources]) -> None:
        """
        Add plot and text on window
        :param resources: the list of resources from last minute
        :return: None
        """
        self._add_graphs(resources)
        self._add_text()

    def _add_graphs(self, resources: List[CPUResources]) -> None:
        """
        Add plot on window
        :param resources: the list of resources from last minute
        :return: None
        """
        seconds = Utils.get_seconds()
        cpu_percents = Utils.get_front_padding(resources) + [
            resource.cpu_percent
            for resource in resources
        ]
        cpu_percents = cpu_percents[::-1]

        Utils.draw_plot(
            self._axes, seconds, cpu_percents,
            'red', 'CPU usage'
        )

    def _add_text(self) -> None:
        """
        Add text on window
        :return: None
        """
        self._axes.set_title('Resource Monitor')
        self._axes.set_ylabel('percent (%)')

        self._axes.set_xlabel('seconds (s)')
        self._axes.xaxis.set_label_position('top')
        self._axes.xaxis.tick_top()

    def clear(self) -> None:
        """
        Clear window
        :return: None
        """
        self._axes.clear()
