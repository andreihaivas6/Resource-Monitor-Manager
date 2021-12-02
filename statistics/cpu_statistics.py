from system_resources.cpu_resources import CPUResources
from .canvas_config import CanvasConfig

import matplotlib.figure
import matplotlib.axes

from typing import List

from .utils import Utils


class CPUStatistics:
    def __init__(self, figure: matplotlib.figure.Figure):
        self._axes: matplotlib.axes.Axes = figure.add_subplot(
            CanvasConfig.NUMBER_ROWS,
            CanvasConfig.NUMBER_COLUMNS,
            CanvasConfig.CPU_POSITION
        )

    def calculate(self, resources: List[CPUResources]) -> None:
        self._add_graphs(resources)
        self._add_text(resources)

    def _add_graphs(self, resources: List[CPUResources]) -> None:
        seconds = Utils.get_seconds(resources)
        cpu_percents = Utils.get_front_padding(resources) + [
            resource.cpu_percent
            for resource in resources
        ]
        cpu_percents = cpu_percents[::-1]

        Utils.draw_plot(
            self._axes, seconds, cpu_percents,
            'red', 'CPU usage'
        )

    def _add_text(self, resources: List[CPUResources]) -> None:
        self._axes.set_title('Resource Monitor')
        self._axes.set_ylabel('percent (%)')

        self._axes.set_xlabel('seconds (s)')
        self._axes.xaxis.set_label_position('top')
        self._axes.xaxis.tick_top()

        # self._axes.invert_xaxis()

        # right_point = len(seconds)
        # self._axes.text(right_point, 8, 'statistici..')

        # self._axes.set_xlabel('seconds (s)')

    def clear(self) -> None:
        self._axes.clear()
