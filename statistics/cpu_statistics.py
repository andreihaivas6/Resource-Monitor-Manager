from system_resources.cpu_resources import CPUResources
from .canvas_config import CanvasConfig

import matplotlib.figure

from typing import List

from .utils import Utils


class CPUStatistics:
    def __init__(self, figure: matplotlib.figure.Figure):
        self._axes = figure.add_subplot(
            CanvasConfig.NUMBER_ROWS,
            CanvasConfig.NUMBER_COLUMNS,
            CanvasConfig.CPU_POSITION
        )

    def calculate(self, resources: List[CPUResources]) -> None:
        seconds = Utils.get_seconds(resources)
        cpu_percents = [0.] * (CanvasConfig.MAX_SECONDS_ON_PLOTS - len(resources)) + [
            resource.cpu_percent
            for resource in resources
        ]

        self._axes.plot(seconds, cpu_percents, 'red')

        self._axes.set_title('Resource Monitor')
        # right_point = len(seconds)
        # self._axes.text(right_point, 8, 'statistici..')
        self._axes.set_ylabel('percent (%)')
        # self._axes.set_xlabel('seconds (s)')

    def clear(self) -> None:
        self._axes.clear()
