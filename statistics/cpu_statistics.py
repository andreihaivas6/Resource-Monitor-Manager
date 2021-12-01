from .canvas_config import CanvasConfig

import matplotlib.figure


class CPUStatistics:
    def __init__(self, figure: matplotlib.figure.Figure):
        self._axes = figure.add_subplot(
            CanvasConfig.NUMBER_ROWS,
            CanvasConfig.NUMBER_COLUMNS,
            CanvasConfig.CPU_POSITION
        )
        self._calculate()

    def _calculate(self):
        self._axes.plot([0, 1, 2, 3, 4], [10, 1, 20, 3, 40])
        self._axes.set_title('titlu')
        self._axes.text(4.5, 8, 'statistici..')
        self._axes.set_ylabel('percent (%)')
