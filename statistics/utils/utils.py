from statistics.utils.canvas_config import CanvasConfig

import matplotlib.axes

from typing import List


class Utils:
    BYTES_ON_KB = 1024

    @staticmethod
    def get_seconds() -> List[int]:
        return [
            second
            for second in range(CanvasConfig.MAX_SECONDS_ON_PLOTS)
        ]

    @staticmethod
    def get_front_padding(resources: list) -> List[float]:
        return [0.] * (CanvasConfig.MAX_SECONDS_ON_PLOTS - len(resources))

    @staticmethod
    def draw_plot(
            axes: matplotlib.axes.Axes, x_list: List[int], y_list: List[float],
            color: str, label: str, alpha: int = 0.4) -> None:
        axes.fill_between(
            x_list,
            y_list,
            color=color,
            alpha=alpha,
        )

        axes.plot(
            x_list,
            y_list,
            color=color,
            label=label,
        )
        if len(label) > 0:
            axes.legend()

    @staticmethod
    def transform_to_gb(my_bytes: int) -> float:
        return round(my_bytes / (Utils.BYTES_ON_KB ** 3), 1)

    @staticmethod
    def transform_bytes(my_bytes: int) -> str:
        values = ['B', 'KB', 'MB', 'GB', 'TB']

        count = 0
        while (my_bytes / Utils.BYTES_ON_KB) > 1:
            my_bytes /= Utils.BYTES_ON_KB
            count += 1

        return f'{round(my_bytes, 1)} {values[count]}'
