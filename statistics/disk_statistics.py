from .canvas_config import CanvasConfig

import matplotlib.figure


class DiskStatistics:
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
        self._calculate()

    def _calculate(self):
        self._axes.plot([0, 1, 2, 3, 4], [10, 1, 20, 3, 40])

        self._pie = self._pie.pie(
            [15, 30],
            explode=[0, 0.1],
            labels=['A', 'B'],
            autopct='%1.1f%%',
            shadow=True,
            startangle=90
        )
