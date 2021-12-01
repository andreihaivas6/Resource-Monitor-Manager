from .canvas_config import CanvasConfig

import matplotlib.figure


class MemoryStatistics:
    def __init__(self, figure: matplotlib.figure.Figure):
        self._axes = figure.add_subplot(
            CanvasConfig.NUMBER_ROWS,
            CanvasConfig.NUMBER_COLUMNS,
            CanvasConfig.MEMORY_POSITION
        )
        self._calculate()

    def _calculate(self):
        self._axes.plot([0, 1, 2, 3, 4], [10, 1, 20, 3, 40])
