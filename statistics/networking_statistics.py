from system_resources.networking_resources import NetworkingResources
from .canvas_config import CanvasConfig
from .utils import Utils

import matplotlib.figure

from typing import List


class NetworkingStatistics:
    def __init__(self, figure: matplotlib.figure.Figure):
        self._axes = figure.add_subplot(
            CanvasConfig.NUMBER_ROWS,
            CanvasConfig.NUMBER_COLUMNS,
            CanvasConfig.NETWORKING_POSITION
        )

    def calculate(self, resources: List[NetworkingResources]) -> None:
        seconds = Utils.get_seconds(resources)
        self._axes.plot([0, 1, 2, 3, 4], [10, 1, 20, 3, 40])

    def clear(self) -> None:
        self._axes.clear()
