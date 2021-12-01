from system_resources.disk_resources import DiskResources
from .canvas_config import CanvasConfig
from .utils import Utils

import matplotlib.figure

from typing import List


class DiskStatistics:
    EXPLODE = [0, 0.1]

    def __init__(self, figure: matplotlib.figure.Figure):
        self._axes = figure.add_subplot(
            CanvasConfig.NUMBER_ROWS,
            CanvasConfig.NUMBER_COLUMNS,
            CanvasConfig.DISK_POSITION
        )
        self._pie = figure.add_subplot(
            CanvasConfig.NUMBER_ROWS,
            CanvasConfig.NUMBER_COLUMNS,
            CanvasConfig.DISK_PIE_POSITION
        )
        self._init_pie = False

    def calculate(self, resources: List[DiskResources]) -> None:
        seconds = Utils.get_seconds(resources)
        self._axes.plot([0, 1, 2, 3, 4], [10, 1, 20, 3, 40])

        if not self._init_pie:
            self._pie = self._pie.pie([
                    resources[0].free_space_percent, resources[0].used_space_percent
                ],
                explode=DiskStatistics.EXPLODE,
                labels=[
                    'Free\n\n', 'Used\n\n'
                ],
                autopct='%1.1f%%',
                shadow=True,
                startangle=90
            )
            self._init_pie = True

    def clear(self) -> None:
        self._axes.clear()
